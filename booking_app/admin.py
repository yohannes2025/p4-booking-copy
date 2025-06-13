from django.contrib import admin
from .models import Restaurant, Table, Booking


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',)
    search_fields = ('name', 'address',)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'table_number', 'capacity',)
    list_filter = ('restaurant',)
    search_fields = ('table_number',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurant', 'table', 'booking_date',
                    'booking_time', 'number_of_guests', 'created_at',)
    list_filter = ('restaurant', 'booking_date', 'booking_time',)
    search_fields = ('user__username', 'restaurant__name',
                     'table__table_number',)
    date_hierarchy = 'booking_date'
