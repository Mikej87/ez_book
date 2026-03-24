from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking, Table

# HOME PAGE


def home(request):
    return render(request, 'booking/home.html')


def menu(request):
    dishes = Dish.objects.all()
    return render(request, 'booking/menu.html', {'dishes': dishes})

# CREATE: User makes a new booking


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ['table', 'booking_date', 'booking_time', 'guest_count']
    template_name = 'booking_form.html'
    success_url = reverse_lazy('my_bookings')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# READ: User views their own reservations


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'my_bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

# UPDATE: User edits a booking


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    fields = ['booking_date', 'booking_time', 'guest_count']
    template_name = 'booking_form.html'
    success_url = reverse_lazy('my_bookings')

# DELETE: User cancels a booking


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('my_bookings')
