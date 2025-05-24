# booking_app/forms.py
from django import forms
from .models import Booking, Restaurant, Table


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['restaurant', 'table', 'booking_date',
                  'booking_time', 'number_of_guests']
        widgets = {
            'booking_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the form to show only available tables
        # for the selected restaurant
        if 'restaurant' in self.data:
            try:
                restaurant_id = int(self.data.get('restaurant'))
                self.fields['table'].queryset = Table.objects.filter(
                    restaurant_id=restaurant_id)
            except (ValueError, TypeError):
                # If there is an error select no tables to display.
                self.fields['table'].queryset = Table.objects.none()
        elif self.instance.pk:
            # If the form has an instance display all tables
            self.fields['table'].queryset = (
                self.instance.restaurant.tables.all()
            )

        # Add a class to the restaurant field for AJAX filtering
        self.fields['restaurant'].widget.attrs.update(
            {'class': 'restaurant-select'})
