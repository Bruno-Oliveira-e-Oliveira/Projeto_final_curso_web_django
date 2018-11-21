function abrirModal() {
    try {
        if (document.getElementsByClassName('msg-form').innerHTML != '') {
            document.getElementById('modal').style.display = "block";
        }   
    } catch (erro) {
        console.log(erro);
    }

}

function a(){
    console.log('ssssssss');
    
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

