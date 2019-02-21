import sys
class Idioma:
	diccionarioMensajes = {}
	#Acá van todos los mensajes en español, tenemos que definir cuáles serán, por el momento pondré el menú inicial
	español = {
	"operacionesInicio": """
		Opciones
		1. Iniciar Sesión
		2. Registrarse
		3. Cambiar Idioma	
		4. Salir
		""",
	"operacionesUsuario": """
		Opciones
		1. Crear Playlist
		2. Playlist propias
		3. Playlist públicas de la plataforma
		4. Cerrar Sesión
		5. Salir
		""",
	"operacionesAdmin": """
		Opciones
		1. Eliminar Usuario
		2. Cambiar Nombre
		3. Ver Usuarios
		4. Dar privilegios de administrador
		5. Cerrar Sesión
		6. Salir
		""",

      "saludo": "Bienvenido a la biblioteca, ",
	"opcion": "¿Qué desea hacer?: ",
	"opcionNoValida": "{0} no es una opción válida",
	"salir": "		Hasta luego, vuelve pronto :c",
	"nombreUs": "Ingrese Usuario: ",
	"idUs": "Ingrese id: ",
	"emailUs": "Ingrese e-mail: ",
	"passwordUs": "Ingrese la contraseña: ",
	"formatoUsuario": "Id: %d Nombre: %s Email: %s ",
	"formatoPlay": "Nombre de la Play list: %s Descripcion: %s Usuario asociado: %s",
	"nombrePL": "Ingrese el nombre de la Playlist: ",
	"formatoCortoPlay": "Nombre de la Playlist: %s Descripcion: %s ",
	"desPL": "Ingrese la descripción de la Playlist: ",
	"nombreUsPlay": "Ingrese Usuario Asociado",
	"MensajeCreacionPlay": "	Has creado una PlayList :3",
	"desPL": "Ingrese la descripción de la Playlist: ",
	"ElId": "Ingrese el id del usuario a eliminar: ",
	"sesExito": "		Sesión iniciada con éxito.",
	"credNo": "		Las credenciales no coinciden.",
	"NoReg": "		El usuario ingresado no está registrado.",
	"UsExiste": "		El usuario ya se encuentra en uso.",
	"EmExiste": "		El email ya se encuentra en uso.",
	"NoUsuElim":"		No hay un usuario con ese id para eliminar.",
	"IdInval": "		El ID ingresado es inválido.",
	"UsuarioAdmin": "		Ingrese el nombre el usuario a privilegiar: ",
	"ElimInva": "	El usuario no se puede eliminar.",
	"newUs": "Ingrese el nuevo nombre de usuario: ",
	"visPlay": "¿Desea que su playlist sea pública o privada? Ingrese 1 para pública o 0 para privada: ",
	"noPlay": "		No hay playlists para mostrar en el momento.",
	"crearPlayExito": "		(Se ha creado la playlist {0} con éxito.)"
	#Acá se van agregando todos los textos que querramos
	}
	
	ingles = {
	"operacionesInicio": """
		Options
		1. Log in
		2. Sign in
		3. Change language
		4. Exit
		""",
	"operacionesUsuario": """
		Opciones
		1. Create Playlist
		2. Log out
		3. Exit
		""",
	"operacionesAdmin": """
		Opciones
		1. Deleter user
		2. Change name
		3. See users
		4. Exit
		""",
		
      "saludo": "Hi ",
	"opcion": "What would you like to do?: ",
	"opcionNoValida": "{0} isn't a valid option",
	"salir": "Bye, see you later",
	"nombreUs": "Enter your username: ",
	"idUs": "Enter your id: ",
	"emailUs": "Enter your e-mail: ",
	"passwordUs": "Enter your password: ",
	"formatoUsuario": "Id: %d Name: %s Email: %.2f ",
	"formatoPlay": "Name of the Play list: %s Description: %s Asociate User: %s",
	"formatoCortoPlay": "Name of the Playlist: %s Description: %s ",
	"nombreUsPlay": "set the user asociate",
	"MensajeCreacionPlay": "you created a PlayList :3",
	"nombrePL": "Enter the Playlist name: ",
	"desPL": "Enter the description of the Playlist: ",
	#El mismo comentario de arriba pero en inglés :v
	}
