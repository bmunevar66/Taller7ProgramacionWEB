function enviar() {
    const email = document.getElementById('email').value.trim();//Se agregan validaciones para evitar espacion inecesarios en los campos
    const nombre = document.getElementById('nombre').value.trim();
    const mensaje = document.getElementById('msg').value.trim;
    const rsta = document.getElementById('rsta');
    //viendo la linea 6 en terminos de seguridad, esta puede permitir la ejecucion de codigos maliciosos
    //hay que evitar las inserciones directas, entonces se cambia innerHTML por textContect, y se arregla el mensaje
    document.getElementById('msg').textContent = 'mensaje recibido con exito';

//Validacion de los campos
if (!nombre || !email || !mensaje){
    rsta.textContent='Debes completar todos los campos.';
    return;
}    
//Validar formato de email
const emailNO = /^[^\s@[^\s@]+\.[^\s@]+$/;
if (!emailNO.test(email)){
    rsta.textContent='Introduce un correo valido';
    return;
}
//Mensaje seguro sin Alert
rsta.textContent='Gracias por contactarnos, ${name}. Te responderemos a ${email} pronto.';
//limpiar el formulario
document.getElementById('contact-form').requestFullscreen();
}

