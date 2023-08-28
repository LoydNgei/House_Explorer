// count.js
const countElements = document.querySelectorAll('.count');

const incrementCount = (element, target) => {
  let count = 0;
  const interval = Math.ceil(target / 100); // Adjust interval for smooth animation

  const increment = () => {
    if (count <= target) {
      element.textContent = count;
      count++;
      setTimeout(increment, interval);
    }
  };

  increment();
};

const startCounting = () => {
  countElements.forEach(element => {
    const target = parseInt(element.getAttribute('data-target'));
    incrementCount(element, target);
  });
};

// Use the Intersection Observer to start counting when the element is in viewport
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      startCounting();
      observer.unobserve(entry.target);
    }
  });
});

countElements.forEach(element => {
  observer.observe(element);
});
