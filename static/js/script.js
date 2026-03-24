document.addEventListener('DOMContentLoaded', function() {
    // 1. Auto-hide Alert Messages (Success/Error)
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 3000);
    });

    // 2. Add Loading State to Booking Button
    const bookingForm = document.querySelector('form');
    if (bookingForm) {
        bookingForm.addEventListener('submit', function() {
            const btn = bookingForm.querySelector('button[type="submit"]');
            if (btn) {
                btn.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Processing...';
                btn.classList.add('disabled');
            }
        });
    }
});