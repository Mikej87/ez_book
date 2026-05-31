from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

class Table(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.table_number} ({self.capacity} seats)"


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name


class Booking(models.Model):
    # FIX 1: Made user optional (null=True, blank=True) and changed CASCADE to SET_NULL
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    guest_count = models.PositiveIntegerField()
    ordered_dishes = models.ManyToManyField(Dish, blank=True, related_name='booked_orders')

    def clean(self):
        super().clean()

        # Prevent past bookings
        if self.booking_date and self.booking_date < timezone.now().date():
            raise ValidationError("You cannot book a table in the past!")

        # Check Table Capacity: Ensure guest count fits the table
        if self.table and self.guest_count > self.table.capacity:
            raise ValidationError(f"This table only seats {self.table.capacity} people.")

        # Check for Overlapping Bookings on the same table and date
        if self.table and self.booking_date:
            overlap = Booking.objects.filter(
                table=self.table,
                booking_date=self.booking_date
            ).exclude(pk=self.pk) # Excludes current booking if updating

            if overlap.exists():
                raise ValidationError("Sorry, this table is already booked for that date.")

    def save(self, *args, **kwargs):
        self.full_clean() # Forces Django Admin and forms to run the clean() validation above
        super().save(*args, **kwargs)

    def __str__(self):
        # FIX 2: Check if user exists before trying to access the username attribute
        username = self.user.username if self.user else "Anonymous Guest"
        return f"{username} - Table {self.table.table_number} on {self.booking_date}"