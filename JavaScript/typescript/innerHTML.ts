onload = () => {
  (document.getElementById('idInnerHTML') as HTMLButtonElement).addEventListener('click', htmlDeDentro);
  (document.getElementById('idAppendChild') as HTMLButtonElement).addEventListener('click', acrescentaFilho);
}

var qtd = 512;

function htmlDeDentro() {
  var inicio = new Date().getTime();
  var idDiv = document.getElementById("idDiv") as HTMLDivElement;
  for(var i=0; i<qtd; i++)
    (document.getElementById("idDiv") as HTMLDivElement).innerHTML += "<input type=text>";
  alert (((new Date().getTime() - inicio) + " ms"));
  let child = idDiv.firstChild;
  while(child) {
    idDiv.removeChild(child);
    child = idDiv.firstChild;
  }
}

function acrescentaFilho() {
  var inicio = new Date().getTime();
  var idDiv = document.getElementById("idDiv") as HTMLDivElement;
  for(var i=0; i<qtd; i++) {
    var campo = document.createElement("input");
    campo.setAttribute("type", "text");
    idDiv.appendChild(campo);
  }
  alert (((new Date().getTime() - inicio) + " ms"));
  let child = idDiv.firstChild;
  while(child) {
    idDiv.removeChild(child);
    child = idDiv.firstChild;
  }
}