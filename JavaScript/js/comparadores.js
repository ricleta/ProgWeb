// It's best practice to declare variables with `let` or `const`
// and to declare them on the line where they are first used.
const a = 5;
const b = 7;
const c = 5;
const d = '5'; // d is a string

// Wait for the HTML document to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', function() {
  // 1. Get the container element from the HTML
  const outputDiv = document.getElementById('output');

  // 2. Build the HTML content in a single string
  let content = '';
  content += `a == b? ${a == b}<br>`;   // false
  content += `a == c? ${a == c}<br>`;   // true
  content += `a === b? ${a === b}<br>`; // false
  content += `a === c? ${a === c}<br>`; // true
  content += `a == d? ${a == d}<br>`;   // true (loose equality converts types)
  content += `a === d? ${a === d}<br>`; // false (strict equality checks type and value)

  // 3. Set the innerHTML of the container once
  outputDiv.innerHTML = content;
});