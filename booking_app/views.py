# booking_app/views.py
# booking_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import JsonResponse  # Import for JSON response
from .models import Booking, Table, Restaurant
from .forms import BookingForm



def home(request):
    restaurants = Restaurant.objects.all()
    # Pass current year for footer
    from datetime import datetime
    current_year = datetime.now().year
    return render(
        request,
        'booking_app/home.html',
        {'restaurants': restaurants, 'current_year': current_year}
    )


@login_required
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            try:
                booking.clean()  # Validate before saving
                booking.save()
                messages.success(request, 'Your booking was successful!')
                return redirect('view_bookings')
            except Exception as e:
                # Catching ValidationError specifically from the clean method
                messages.error(request, f'There was an error: {e}')
        else:
            # If form is not valid, messages will display errors automatically with Crispy Forms
            pass
    else:
        form = BookingForm()
    return render(request, 'booking_app/book_table.html', {'form': form})


@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by(
        '-booking_date', '-booking_time')
    # Pass current year for footer
    from datetime import datetime
    current_year = datetime.now().year
    return render(
        request,
        'booking_app/view_bookings.html',
        {'bookings': bookings, 'current_year': current_year}
    )


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Your booking has been cancelled.')
        return redirect('view_bookings')
    # Pass current year for footer
    from datetime import datetime
    current_year = datetime.now().year
    return render(
        request,
        'booking_app/cancel_booking.html',
        {'booking': booking, 'current_year': current_year}
    )


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            # Redirect to login after registration
            return redirect('account_login')
        else:
            # If form is not valid, messages will display errors automatically
            pass
    else:
        form = UserCreationForm()
    # Pass current year for footer
    from datetime import datetime
    current_year = datetime.now().year
    return render(request, 'booking_app/register.html', {'form': form, 'current_year': current_year})


def get_tables_for_restaurant(request, restaurant_id):
    """
    API endpoint to return tables for a given restaurant as JSON.
    """
    try:
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        tables = Table.objects.filter(restaurant=restaurant).values(
            'id', 'table_number', 'capacity')
        return JsonResponse(list(tables), safe=False)
    except Restaurant.DoesNotExist:
        return JsonResponse({'error': 'Restaurant not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
