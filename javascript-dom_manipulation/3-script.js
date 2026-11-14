const head = document.querySelector('header');
const toggleHeader = document.querySelector('#toggle_header');

toggleHeader.addEventListener('click', () => {
  if (head.classList.contains('green')) {
    head.classList.replace('green', 'red');
  } else {
    head.classList.replace('red', 'green');
  }
});
