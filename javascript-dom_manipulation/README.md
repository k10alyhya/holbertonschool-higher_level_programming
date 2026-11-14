# JavaScript - DOM Manipulation

Scripts that select, modify and update HTML elements in the browser using the Document Object Model (DOM), listen to user and DOM events, and fetch data from external APIs with the Fetch API.

## Learning Objectives

- How to select HTML elements in JavaScript
- What are differences between ID, class and tag name selectors
- How to modify an HTML element style
- How to get and update an HTML element content
- How to modify the DOM
- How to make a request with XmlHTTPRequest
- How to make a request with Fetch API
- How to listen/bind to DOM events
- How to listen/bind to user events

## Requirements

- Scripts are interpreted in the browser
- Code follows `semistandard` style
- All files end with a new line

## Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `0-script.js` | Updates the text color of the `header` element to red (`#FF0000`) using `document.querySelector` |
| 1 | `1-script.js` | Updates the text color of the `header` element to red when the user clicks on `#red_header` |
| 2 | `2-script.js` | Adds the class `red` to the `header` element when the user clicks on `#red_header` |
| 3 | `3-script.js` | Toggles the `header` class between `red` and `green` when the user clicks on `#toggle_header` |
| 4 | `4-script.js` | Adds a new `<li>Item</li>` to the `.my_list` list when the user clicks on `#add_item` |
| 5 | `5-script.js` | Updates the text of the `header` element to `New Header!!!` when the user clicks on `#update_header` |
| 6 | `6-script.js` | Fetches a Star Wars character name with the Fetch API and displays it in `#character` |
| 7 | `7-script.js` | Fetches all Star Wars movie titles and lists them in `#list_movies` |
| 8 | `8-script.js` | Fetches the French translation of "hello" and displays it in `#hello`; works when loaded from `<head>` |

## Usage

Open the matching `X-main.html` file in a browser. Each HTML file loads its script with a `<script>` tag.

Tasks 6 to 8 use the Fetch API, so serve the folder with a local server (for example, VS Code Live Server) instead of opening the file directly.

## Concepts Used

| Concept | Methods / Properties | Tasks |
|---------|----------------------|-------|
| Selecting elements | `querySelector` | 0-8 |
| Changing style | `style.color`, `classList.add`, `classList.contains`, `classList.replace` | 0-3 |
| Changing content | `textContent` | 4-8 |
| Modifying the DOM | `createElement`, `appendChild` | 4, 7 |
| User events | `addEventListener('click', ...)` | 1-5 |
| DOM events | `addEventListener('DOMContentLoaded', ...)` | 8 |
| Network requests | `fetch`, `.then`, `.catch`, `response.json()` | 6-8 |

## Author

Khaled Al-Yahya