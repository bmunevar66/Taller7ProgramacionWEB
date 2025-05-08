import os
from zipfile import ZipFile

# Definir ruta del proyecto
project_path = "../Taller7ProgramacionWEB/Proyecto_Web_Erroneo_Extendido2"

# Crear carpeta si no existe
os.makedirs(project_path, exist_ok=True)

# Contenido de los archivos (puedes personalizar esto)
more_html = more_html = """<!DOCTYPE html>
<html>
<head>
    <title>Formulario de Contacto</title>
    <link rel="stylesheet" href="contact.css">
</head>
<body>
    <h2>Contáctanos</h2>
    <form id="contact-form" onsubmit="enviar(); return false;">
        <label for="name">Nombre</label>
        <input type="text" id="name"><br>

        <label for="email">Correo</label>
        <input type="text" id="email"><br>

        <label for="msg">Mensaje</label>
        <textarea id="msg"></textarea><br>

        <button type="submit">Enviar</button>
    </form>
    <script src="contact.js"></script>
</body>
</html>
"""

contact_css = """h2 {
    color: lime;
    background-color: black;
}
form {
    width: 150%;
    padding: 50px;
}
label, input, textarea {
    display: block;
    margin-bottom: 20px;
}
"""


contact_js = """function enviar() {
    let email = document.getElementById('email').value;
    alert("Gracias por contactarnos " + email);
    document.getElementById('msg').innerHTML = "<script>alert('XSS en mensaje')</script>";
}
"""


# Guardar los archivos
with open(os.path.join(project_path, "contact.html"), "w", encoding="utf-8") as f:
    f.write(more_html)

with open(os.path.join(project_path, "contact.css"), "w", encoding="utf-8") as f:
    f.write(contact_css)

with open(os.path.join(project_path, "contact.js"), "w", encoding="utf-8") as f:
    f.write(contact_js)

# Crear el archivo ZIP con el proyecto
extended_zip_path = "/mnt/data/Proyecto_Web_Erroneo_Extendido.zip"
with ZipFile(extended_zip_path, 'w') as zipf:
    for root, _, files in os.walk(project_path):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, project_path)
            zipf.write(file_path, arcname=arcname)

print(f"Proyecto empaquetado en: {extended_zip_path}")

