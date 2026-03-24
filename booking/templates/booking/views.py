from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Booking, Table

# Create: User makes a booking


class BookingCreateView(CreateView):
    model = Booking
    fields = ['table', 'booking_date', 'booking_time', 'guest_count']
    template_name = 'booking_form.html'
    success_url = reverse_lazy('my_bookings')

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

# Read: User views their history


class BookingListView(ListView):
    model = Booking
    template_name = 'my_bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(customer=self.request.user)

# Update & Delete: Edit/Cancel functionality


class BookingUpdateView(UpdateView):
    model = Booking
    fields = ['booking_date', 'booking_time', 'guest_count']
    template_name = 'booking_form.html'
    success_url = reverse_lazy('my_bookings')


class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('my_bookings')