document.addEventListener("DOMContentLoaded", () => {
    // Mobile Menu Toggle
    const mobileMenu = document.getElementById('mobile-menu');
    const navLinks = document.getElementById('nav-links');
    const navItems = document.querySelectorAll('.nav-item');

    if (mobileMenu && navLinks) {
        mobileMenu.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });

        // Close menu when clicking a link
        navItems.forEach(item => {
            item.addEventListener('click', () => {
                if (navLinks.classList.contains('active')) {
                    navLinks.classList.remove('active');
                }
            });
        });
    }

    // Select elements to reveal on scroll
    const revealElements = document.querySelectorAll('.project-card, .skill-card, .details-content, .hero > *');

    revealElements.forEach(el => {
        el.classList.add('reveal-item');
    });

    // Highly optimized observer
    const observerOptions = {
        root: null,
        rootMargin: '100px', // Trigger well before they come into view to avoid pop-in lag
        threshold: 0
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Instantly add the class, let CSS handle a simple opacity change
                entry.target.classList.add('revealed');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    revealElements.forEach(el => {
        revealObserver.observe(el);
    });
});
