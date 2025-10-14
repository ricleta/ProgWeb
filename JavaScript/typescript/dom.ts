onload = () => {
  (document.getElementById('add-phone') as HTMLButtonElement).addEventListener('click', addPhone);
}

function addPhone() {
    var campo = document.createElement("input");
    campo.setAttribute("type", "text");
    campo.setAttribute("name", "phone");

    var botaoRemover = document.createElement("button");
    botaoRemover.textContent = "Remove";
    botaoRemover.type = "button"; // Prevent form submission
    botaoRemover.addEventListener('click', function() {
        (this.parentNode as HTMLDivElement).remove();
    });

    // The styling is now handled by css/style.css
    var div = document.createElement("div");
    div.appendChild(campo);
    div.appendChild(botaoRemover);
    (document.getElementById("phones") as HTMLDivElement).appendChild(div);
}

function removePhone(button: HTMLButtonElement) {
    (button.parentNode as HTMLDivElement).remove();
}