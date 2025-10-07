onload = function ()
{
  let objNome = this.document.getElementById("name");
  let objN1 = this.document.getElementById("n1");
  let objN2 = this.document.getElementById("n2");
  let objResult = this.document.getElementById("result");

  // Create a reusable function for the shuffling logic.
  function shuffleName() {
    // Using an arrow function for a more concise sort.
    let shuffledName = objNome.value.split('').sort(() => 0.5 - Math.random()).join('');
    objNome.value = shuffledName;
  }

  // Add a listener for the 'change' event.
  objNome.addEventListener("change", shuffleName);

  // Add a listener for the 'keydown' event (without the "on" prefix).
  objNome.addEventListener("keydown", shuffleName);

  function calculateSum() {
    const n1 = parseFloat(objN1.value);
    const n2 = parseFloat(objN2.value);

    // Check if the inputs are valid numbers before calculating.
    if (!isNaN(n1) && !isNaN(n2)) {
      const result = n1 + n2;
      objResult.textContent = `${result}`; // Use textContent to display in the div.
    } else {
      objResult.textContent = ""; // Clear the result if inputs are not valid numbers
    }
  }
  
  // Use the 'input' event to get the value after it has changed.
  objN1.addEventListener("input", calculateSum);
  objN2.addEventListener("input", calculateSum);

}