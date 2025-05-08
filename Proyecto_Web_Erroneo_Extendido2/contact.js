function enviar() {
    const email = document.getElementById('email').value.trim();//Se agregan validaciones para evitar espacion inecesarios en los campos
    const nombre = document.getElementById('nombre').value.trim();
    const mensaje = document.getElementById('msg').value.trim;
    const rsta = document.getElementById('rsta');
    //viendo la linea 6 en terminos de seguridad, esta puede permitir la ejecucion de codigos maliciosos
    //hay que evitar las inserciones directas, entonces se cambia innerHTML por textContect, y se arregla el mensaje
    document.getElementById('msg').textContent = 'mensaje recibido con exito';
}
//y se agrega una nueva funcion para la validacion de los datos del formulario
function validarFormulario(){
    let nombre = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    if(!nombre || !email){
        alert('Los campos no pueden estar vacios');
        return false;
    }
}return true;
