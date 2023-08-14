# JavaScript Cheat Sheet

1. Basics:
   - JavaScript is a high-level, interpreted programming language.
   - It is used for adding interactivity to web pages.

2. Variables and Data Types:
   - var, let, and const are used to declare variables.
   - Data types: string, number, boolean, null, undefined, object, symbol.
   - Example:
     let name = "John";
     const age = 30;
     var isStudent = true;

3. Operators:
   - Arithmetic: +, -, *, /, %, **
   - Comparison: ==, ===, !=, !==, >, <, >=, <=
   - Logical: && (and), || (or), ! (not)

4. Control Flow:
   - if, else if, else statements for conditional branching.
   - switch statement for multiple cases.
   - for, while, do-while loops for iteration.

5. Functions:
   - Declare functions using the function keyword.
   - Arrow functions: (parameters) => expression.
   - Example:
     function greet(name) {
       return "Hello, " + name;
     }

6. Arrays:
   - Create arrays using [].
   - Access elements with index (0-based).
   - Array methods: push, pop, shift, unshift, splice, slice, forEach, map, filter.
   - Example:
     let numbers = [1, 2, 3, 4, 5];

7. Objects:
   - Create objects using {}.
   - Access properties using dot notation or bracket notation.
   - Example:
     let person = {
       name: "Alice",
       age: 25,
       isStudent: false,
     };

8. Classes and Objects (ES6):
   - Create classes using class keyword.
   - Use constructor for initializing properties.
   - Example:
     class Person {
       constructor(name, age) {
         this.name = name;
         this.age = age;
       }
     }

9. Promises and Async/Await (ES6):
   - Promises are used for asynchronous operations.
   - Async functions with the await keyword.
   - Example:
     function fetchData() {
       return new Promise((resolve, reject) => {
         // ... asynchronous operation
       });
     }

10. DOM Manipulation:
    - Document Object Model (DOM) is a representation of the web page's structure.
    - Manipulate elements using JavaScript to create interactivity.
    - Example:
      let element = document.getElementById("myElement");
      element.innerHTML = "New content";

11. Events:
    - Attach event listeners to elements.
    - Common events: click, submit, keyup, etc.
    - Example:
      document.getElementById("myButton").addEventListener("click", function() {
        alert("Button clicked!");
      });

12. Error Handling:
    - Use try...catch blocks to handle exceptions.
    - Example:
      try {
        // code that might throw an error
      } catch (error) {
        console.error("An error occurred:", error);
      }