# Blog de Recetas
## Development

### Integrantes:
- Renzo Castiglione
    - Modelos, vistas, formularios, plantillas html.
- Ricardo López

### Modelos
- Entrada
    - Titulo
    - Subtitulo
    - Autor
    - Fecha
    - Cuerpo
    - Imagen
    - Likes
- Mensaje
    - Emisor
    - Remitente
    - Cuerpo
    - Leido

### Formularios
- Los formularios para ingresar datos en los modelos se encuentran implementados (Entrada, Mensaje)
- Los formularios para editar datos se encuentran implementados (Entrada, Usuario) (Como una restricción del sistema, establecida por nosotros, los mensajes no se pueden editar)

### Funcionalidades

#### Entradas
- Página de inicio
    - En la página de inicio se encuentran 4 entradas, que van variando de forma aleatoria ( función implementada ).
    - Se puede acceder al login, al registro de usuario y logout(en caso de usuario autenticado).
    - Se puede acceder al listado de todas las entradas.
    - Se puede acceder a una de las entradas mostradas para continuar leyendo.
    - Por cada entrada se muestra el autor y la fecha, así como título y subtítulo, y una imágen ( Excepto en el caso de la entrada que encabeza el inicio ).
    - Se muestra una sección de información sobre el blog ( 'About' ).
- Listado de todas las entradas
    - Se muestran todas las entradas, con sus respectivos título, subtítulo, autor, fecha, y una imagén de portada.
    - En la entrada se muestran botones para:
        - Ver la entrada completa.
        - Editar ( en caso de ser el autor y estar autenticado ).
        - Eliminar ( en caso de ser el autor y estar autenticado ).
        - Dar 'Me gusta' ( se debe estar logueado ).
- Nueva entrada
    - Se muestra un formulario para crear una nueva entrada con Título, subtitulo, cuerpo y una imágen obligatoria de portada. ( se pueden agregar más a través del editor de texto en el cuerpo ).
- Editar Entrada
    - Se muestra un formulario para editar la entrada elegida.
- Eliminar entrada
    - Se redirecciona a una página de confirmación, y luego (en caso afirmativo) se elimina la entrada.
- Mostrar entrada
    - Se muestra la entrada completa.
    - Se muestra un botón de 'Me gusta' al final
    - En caso de ser el autor también se muestran botones para editar o eliminar la entrada.
- Favoritos
    - Se muestran las entradas a las que el usuario les dió 'Me gusta'.
- Mis recetas
    - Se muestran las entradas creadas por el usuario.

#### Mensajes
- Bandeja de entrada
    - Se muestran todos los mensajes del usuario.
    - Por cada mensaje se muestra un botón para ver el mensaje completo y eliminar el mensaje.
- Nuevo mensaje
    - Se muestra un formulario para envíar un nuevo mensaje con, destinatario, asunto y un cuerpo.
- Ver mensaje
    - Se muestra el mensaje completo, y si el usuario remitente lo leyó.

#### Usuarios
- Formulario de registro
    - Se muestra un formulario para crear un nuevo usuario, con: Nombre de usuario, email, contraseña, nombre y apellido.
- Login
    - Formulario para autenticarse como usuario del sitio e iniciar sesión.
- Editar perfil
    - Se muestra un formulario para editar la información del usuario: email, contraseña, nombre y apellido.

#### NavBar
- Un enlace para volver a la página de inicio.
- Botón de login/registro y logout(con sesión iniciada)
- Menú :
    - Administrador
    - Ver todas las recetas
    - Ver mis recetas
    - Ver mis recetas favoritas
    - Editar mi perfil
    - Mensajes ( app mensajeria )

## Requerimientos
- Se deben tener instalado los siguientes paquetes:
    - django==4.1
    - django-ckeditor
    - django_cleanup
    - Pillow

## Enlace a Video

https://youtu.be/ajyookkwIiU