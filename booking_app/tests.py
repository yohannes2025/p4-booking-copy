from django.test import TestCase
from django.contrib.auth.models import User
from .models import Restaurant, Table, Booking
from django.core.exceptions import ValidationError
from datetime import date, time


class RestaurantTestCase(TestCase):
    def test_restaurant_creation(self):
        restaurant = Restaurant.objects.create(
            name="Test Restaurant", address="123 Main St")
        self.assertEqual(str(restaurant), "Test Restaurant")


class TableTestCase(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant", address="123 Main St")

    def test_table_creation(self):
        table = Table.objects.create(
            restaurant=self.restaurant, table_number=1, capacity=4)
        self.assertEqual(str(table), "Table 1 at Test Restaurant")


class BookingTestCase(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant", address="123 Main St")
        self.table = Table.objects.create(
            restaurant=self.restaurant, table_number=1, capacity=4)
        self.user = User.objects.create_user(
            username="testuser", password="testpass")

    def test_booking_creation(self):
        booking = Booking.objects.create(
            restaurant=self.restaurant,
            table=self.table,
            user=self.user,
            booking_date=date(2025, 5, 1),
            booking_time=time(18, 0),
            number_of_guests=2
        )
        self.assertEqual(
            str(booking), "Booking for 2 at 18:00:00 on 2025-05-01")

    def test_double_booking_validation(self):
        Booking.objects.create(
            restaurant=self.restaurant,
            table=self.table,
            user=self.user,
            booking_date=date(2025, 5, 1),
            booking_time=time(18, 0),
            number_of_guests=2
        )

        with self.assertRaises(ValidationError):
            Booking.objects.create(
                restaurant=self.restaurant,
                table=self.table,
                user=self.user,
                booking_date=date(2025, 5, 1),
                booking_time=time(18, 0),
                number_of_guests=2
            )
