const stars = document.querySelectorAll('.star');

stars.forEach(star => {
  star.addEventListener('click', () => {
    const value = parseInt(star.getAttribute('data-value'));

    stars.forEach((s, index) => {
      if (index < value) {
        s.classList.add('active');
      } else {
        s.classList.remove('active');
      }
    });
  });
});