document.addEventListener('DOMContentLoaded', () => {
    
    //  Dynamic Navbar Background
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.backgroundColor = 'rgba(33, 37, 41, 0.95)'; // Matches your --dark-bg
            navbar.style.transition = '0.3s ease';
        } else {
            navbar.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
        }
    });

    //  Booking Form Handling
    const bookingForm = document.getElementById('reservation-create-form');
    if (bookingForm) {
        bookingForm.addEventListener('submit', (e) => {
            // Prevent actual reload for demo purposes
            e.preventDefault();
            
            // Basic feedback loop
            const submitBtn = bookingForm.querySelector('.btn-primary');
            const originalText = submitBtn.innerText;
            
            submitBtn.innerText = 'Booking...';
            submitBtn.disabled = true;

            setTimeout(() => {
                alert('Table booked successfully!');
                submitBtn.innerText = originalText;
                submitBtn.disabled = false;
                bookingForm.reset();
            }, 1500);
        });
    }

    // Scroll for Nav Links
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            if (this.hash !== "") {
                e.preventDefault();
                const hash = this.hash;
                document.querySelector(hash).scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});