from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()  # Multiple table occupancies

    def __str__(self):
        return f"Table {self.table_number} ({self.capacity} seats)"


class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    guest_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Logic to Avoid Double Bookings
        existing_bookings = Booking.objects.filter(
            table=self.table,
            booking_date=self.booking_date,
            booking_time=self.booking_time
        ).exclude(pk=self.pk)       
        if existing_bookings.exists():
            raise ValidationError("This table is already booked for this time.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
