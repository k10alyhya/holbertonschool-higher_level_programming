document.addEventListener('DOMContentLoaded', () => {
  const myList = document.querySelector('.my_list');
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');

  addItem.addEventListener('click', () => {
    const li = document.createElement('li');
    li.textContent = 'Item';
    myList.appendChild(li);
  });

  removeItem.addEventListener('click', () => {
    const last = myList.lastElementChild;
    if (last) {
      last.remove();
    }
  });

  clearList.addEventListener('click', () => {
    myList.textContent = '';
  });
});
