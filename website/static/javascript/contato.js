function abrirModal() {
    try {
        if (document.getElementsByClassName('msg-form').innerHTML != '') {
            document.getElementById('modal').style.display = "block";
        }   
    } catch (erro) {
        console.log(erro);
    }

}

function fecharModal() {
    document.getElementById('modal').style.display = "none";
}

window.onclick = function(event) {
    var modal = document.getElementById('modal');
    if (event.target == modal) {
        fecharModal();
    }
}

window.onload = function(event){
    var modal = document.getElementById("modal-msg");
    if (modal.innerHTML != '') {
        abrirModal()
    }
    
}



