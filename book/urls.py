from django.contrib import admin
from django.urls import path, include
from booking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # For login/logout
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('bookings/', views.BookingListView.as_view(), name='my_bookings'),
    path('bookings/new/', views.BookingCreateView.as_view(), name='booking_create'),
    path('bookings/<int:pk>/edit/', views.BookingUpdateView.as_view(), name='booking_edit'),
    path('bookings/<int:pk>/delete/', views.BookingDeleteView.as_view(), name='booking_delete'),
]







