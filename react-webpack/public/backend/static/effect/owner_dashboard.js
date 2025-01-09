const ctx = document.getElementById('visitorChart').getContext('2d');
const visitorChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Aug 2018', 'Sep 2018', 'Oct 2018', 'Nov 2018', 'Dec 2018', 'Jan 2019', 'Feb 2019', 'Mar 2019', 'Apr 2019', 'May 2019'],
        datasets: [{
            label: 'Visitors',
            data: [500, 600, 800, 900, 1200, 1500, 1800, 2000, 2200, 2345],
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 2,
            fill: false,
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: { beginAtZero: true },
            y: { beginAtZero: true }
        }
    }
});


document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.querySelector('.field-carousel');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    // Ensure all elements are present
    if (!carousel || !prevBtn || !nextBtn) {
        console.error('Carousel or buttons are not found.');
        return;
    }

    let scrollAmount = 0; // Track the scroll position
    const fieldWidth = carousel.querySelector('.field-item').offsetWidth + 20; // Width of each field including gap
    const maxScroll = (carousel.children.length - 3) * fieldWidth; // Calculate max scroll position

    // Scroll left
    prevBtn.addEventListener('click', () => {
        scrollAmount -= fieldWidth * 3; // Scroll 3 items at a time
        if (scrollAmount < 0) scrollAmount = 0; // Prevent scrolling past the start
        carousel.style.transform = `translateX(-${scrollAmount}px)`;
    });

    // Scroll right
    nextBtn.addEventListener('click', () => {
        scrollAmount += fieldWidth * 3; // Scroll 3 items at a time
        if (scrollAmount > maxScroll) scrollAmount = maxScroll; // Prevent scrolling past the end
        carousel.style.transform = `translateX(-${scrollAmount}px)`;
    });
});
