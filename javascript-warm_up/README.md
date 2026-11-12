# JavaScript - Warm up

Introductory JavaScript scripting project from the Holberton School curriculum.
All scripts run from the command line with Node.js.

## Learning objectives

- How to run a JavaScript script
- How to create variables and constants
- The differences between `var`, `const` and `let`
- The data types available in JavaScript
- How to use `if` and `if ... else` statements
- How to use comments
- How to use `while` and `for` loops
- What a function is and how to use it
- What a function returns when it has no `return` statement
- The scope of variables
- The arithmetic operators and how to use them
- How to manipulate an object (dictionary)
- How to import a file

## Requirements

- Ubuntu 20.04 LTS
- Node.js 14.x
- Code style: `semistandard` 16.x
- The first line of every file is `#!/usr/bin/node`
- All files are executable
- `var` is not used

## Usage

```bash
chmod u+x <file>.js
./<file>.js [arguments]
```

Check the code style:

```bash
semistandard <file>.js
```

## Tasks

| File | Description |
| --- | --- |
| `0-javascript_is_amazing.js` | Prints `JavaScript is amazing` from a constant named `myVar` |
| `1-multi_languages.js` | Prints three lines: `C is fun`, `Python is cool`, `JavaScript is amazing` |
| `2-arguments.js` | Prints `No argument`, `Argument found` or `Arguments found` depending on the number of arguments |
| `3-value_argument.js` | Prints the first argument, or `No argument` if none is passed (without using `length`) |
| `4-concat.js` | Prints two arguments in the format `<first> is <second>` |
| `5-to_integer.js` | Prints `My number: <n>` if the first argument converts to an integer, otherwise `Not a number` |
| `6-multi_languages_loop.js` | Prints the three lines of task 1 using an array and a loop |
| `7-multi_c.js` | Prints `C is fun` x times, where x is the first argument |
| `8-square.js` | Prints a square of `X` characters whose size is the first argument |
| `9-add.js` | Prints the sum of two integers using a function `add(a, b)` |
| `10-factorial.js` | Computes and prints the factorial of the first argument recursively |
| `11-second_biggest.js` | Prints the second biggest integer in the list of arguments |
| `12-object.js` | Updates the `value` property of an object from 12 to 89 |
| `13-add.js` | Exports a function `add` that returns the sum of two integers |

## Examples

```bash
$ ./2-arguments.js Best School
Arguments found

$ ./5-to_integer.js 89.89
My number: 89

$ ./8-square.js 3
XXX
XXX
XXX

$ ./10-factorial.js 3
6

$ ./11-second_biggest.js 4 2 5 3 0 -3
4
```

## Author

Khaled Al-Yahya
