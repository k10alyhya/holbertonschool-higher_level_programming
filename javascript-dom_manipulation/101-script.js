document.addEventListener('DOMContentLoaded', () => {
  const languageCode = document.querySelector('#language_code');
  const btnTranslate = document.querySelector('#btn_translate');
  const hello = document.querySelector('#hello');

  btnTranslate.addEventListener('click', () => {
    const code = languageCode.value;

    fetch(`https://hellosalut.stefanbohacek.com/?lang=${code}`)
      .then((response) => response.json())
      .then((data) => {
        hello.textContent = data.hello;
      })
      .catch((error) => console.error(error));
  });
});
