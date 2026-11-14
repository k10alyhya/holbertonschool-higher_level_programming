const head = document.querySelector('header');
const updateHeader = document.querySelector('#update_header');

updateHeader.addEventListener('click', () => {
  head.textContent = 'New Header!!!';
});
