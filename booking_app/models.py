# booking_app/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Table(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='tables')
    table_number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number} at {self.restaurant.name}"


class Booking(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='bookings')
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_of_guests = models.IntegerField()
    # Automatically set on creation
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Booking for {self.number_of_guests} at {self.booking_time} "
            f"on {self.booking_date}"
        )

    def clean(self):
        # Prevent double bookings
        if self.table and self.booking_date and self.booking_time:
            conflicting_bookings = Booking.objects.filter(
                table=self.table,
                booking_date=self.booking_date,
                booking_time=self.booking_time
            ).exclude(pk=self.pk)  # Exclude the current booking if updating

            if conflicting_bookings.exists():
                raise ValidationError(
                    "This table is already booked for this date and time.")
        super().clean()  # Call the parent's clean() method

    def save(self, *args, **kwargs):
        self.clean()  # Run validation
        super().save(*args, **kwargs)
