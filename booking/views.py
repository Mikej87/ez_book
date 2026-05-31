from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Booking, Table, Dish

# HOME PAGE

def home(request):
    return render(request, 'booking/home.html')

def menu(request):
    dishes = Dish.objects.all()
    return render(request, 'booking/menu.html', {'dishes': dishes})

# CREATE: User makes a new booking

class BookingCreateView(CreateView):
    model = Booking
    # FIX: Using only fields that actually exist in your model
    fields = ['table', 'booking_date', 'guest_count']
    template_name = 'booking/booking_form.html'
    success_url = reverse_lazy('my_bookings')

# READ: User views their own reservations

class BookingListView(ListView):
    model = Booking
    template_name = 'booking/my_bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.all()

# UPDATE: User edits a booking

class BookingUpdateView(UpdateView):
    model = Booking
    # FIX: Match the valid field list here too
    fields = ['booking_date', 'guest_count']
    template_name = 'booking/booking_form.html'
    success_url = reverse_lazy('my_bookings')

# DELETE: User cancels a booking

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking/booking_confirm_delete.html'
    success_url = reverse_lazy('my_bookings')