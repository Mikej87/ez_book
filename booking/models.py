from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField() # e.g., 2, 4, or 6 guests

    def __str__(self):
        return f"Table {self.table_number} ({self.capacity} seats)"

class Booking(models.Model):
    # Relationship: Each booking belongs to a User and a Table
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    guest_count = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        overlap = Booking.objects.filter(
            table=self.table,
            booking_date=self.booking_date,
            booking_time=self.booking_time
        ).exclude(pk=self.pk)

        
class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True) # Optional description
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name        
        
        if overlap.exists():
            raise ValidationError("Sorry, this table is already booked for that time.")

        # 2. Check Capacity: Ensure guest count fits the table
        if self.guest_count > self.table.capacity:
            raise ValidationError(f"This table only seats {self.table.capacity} people.")

        # 3. Prevent past bookings
        if self.booking_date < timezone.now().date():
            raise ValidationError("You cannot book a table in the past!")

    def save(self, *args, **kwargs):
        self.full_clean() # Runs the clean() method above before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - Table {self.table.table_number} on {self.booking_date}"