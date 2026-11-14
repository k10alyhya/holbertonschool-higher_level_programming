const additem = document.querySelector('#add_item');

const mylist = document.querySelector('.my_list');

additem.addEventListener('click', () => {
  const newElement = document.createElement('li');
  newElement.textContent = 'Item';
  mylist.appendChild(newElement);
});
