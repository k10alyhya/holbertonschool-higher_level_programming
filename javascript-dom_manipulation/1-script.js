const head = document.querySelector("header");
const headEvent = document.querySelector("#red_header");

headEvent.addEventListener("click", () => {
    head.style.color = "#FF0000";
});