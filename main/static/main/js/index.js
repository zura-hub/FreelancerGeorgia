const carouselInner = document.querySelector('.carousel-inner');
const carouselItems = document.querySelectorAll('.carousel-item');
const slideInterval = 3000; // Interval between slides in milliseconds

let currentIndex = 0;
let intervalId;

// Function to show the next item in the carousel
function showNextItem() {
  currentIndex = (currentIndex + 1) % carouselItems.length;
  updateCarousel();
}

// Function to update the carousel to show the current item
function updateCarousel() {
  carouselInner.style.transform = `translateX(-${currentIndex * 100}%)`;
}

// Function to start the automatic carousel
function startCarousel() {
  intervalId = setInterval(showNextItem, slideInterval);
}

// Function to stop the automatic carousel
function stopCarousel() {
  clearInterval(intervalId);
}

// Start the automatic carousel
startCarousel();



