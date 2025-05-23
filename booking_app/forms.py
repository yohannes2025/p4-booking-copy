# booking_app/forms.py
from django import forms
from .models import Booking, Restaurant, Table
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Field, HTML


class BookingForm(forms.ModelForm):
    # Added queryset to limit choices to available restaurants/tables if needed
    # For simplicity, I'm keeping them as is, but in a real app, you'd filter these.
    restaurant = forms.ModelChoiceField(
        queryset=Restaurant.objects.all(),
        label="Select a Restaurant",
        empty_label="Choose a restaurant",
        widget=forms.Select(
            attrs={'aria-label': 'Select a restaurant from the list'})
    )
    table = forms.ModelChoiceField(
        # Consider filtering this based on selected restaurant (via JS/Ajax)
        queryset=Table.objects.all(),
        label="Select a Table",
        empty_label="Choose a table",
        widget=forms.Select(attrs={'aria-label': 'Select an available table'})
    )
    booking_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',  # HTML5 date input for better native date picker
            'class': 'form-control',
            'aria-label': 'Booking date',
            'placeholder': 'YYYY-MM-DD'
        }),
        label="Preferred Date"
    )
    booking_time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',  # HTML5 time input
            'class': 'form-control',
            'aria-label': 'Booking time',
            'placeholder': 'HH:MM'
        }),
        label="Preferred Time"
    )
    number_of_guests = forms.IntegerField(
        min_value=1,
        label="Number of Guests",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'aria-label': 'Number of guests for the booking',
            'min': '1'
        })
    )

    class Meta:
        model = Booking
        fields = ['restaurant', 'table', 'booking_date',
                  'booking_time', 'number_of_guests']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Make Your Reservation',
                Field('restaurant'),
                Field('table'),
                Field('booking_date'),
                Field('booking_time'),
                Field('number_of_guests', css_class='form-control'),
                HTML("""<p class="text-muted small mt-2">
                    Please ensure the selected table can accommodate your party size.
                    Availability will be checked upon submission.
                </p>""")
            ),
            Submit('submit', 'Confirm Booking',
                   css_class='btn btn-primary mt-3')
        )

        # Add Bootstrap classes for better styling consistency
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.NumberInput, forms.DateInput, forms.TimeInput, forms.Select)):
                field.widget.attrs['class'] = 'form-control'
            if field.required:
                field.widget.attrs['aria-required'] = 'true'
