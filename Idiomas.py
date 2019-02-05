class Idioma:
	diccionarioMensajes = {}
	#Acá van todos los mensajes en español, tenemos que definir cuáles serán, por el momento pondré el menú inicial
	español = {
	"operaciones": """
		Opciones
		1. Registrarse
		2. Cambiar Nombre
		3. Ver Usuarios
		4. Crear Playlist
		5. Salir
		""",
      "saludo": "Hola ",
	"opcion": "¿Qué desea hacer?: ",
	"opcionNoValida": "{0} no es una opción válida",
	"salir": "Hasta luego, vuelve pronto :c",
	"nombreUs": "Ingrese Usuario: ",
	"idUs": "Ingrese id: ",
	"emailUs": "Ingrese e-mail: ",
	"passwordUs": "Ingrese la contraseña: ",
	"nombrePL": "Ingrese el nombre de la Playlist: ",
	"desPL": "Ingrese la descripción de la Playlist: "
	#Acá se van agregando todos los textos que querramos
	}
	
	ingles = {
	"operaciones": """
		Options
		1. Sign up
		2. Rename
		3. See user
		4. Create Playlist
		5. Exit
		""",
      "saludo": "Hi ",
	"opcion": "What would you like to do?: ",
	"opcionNoValida": "{0} isn't a valid option",
	"salir": "Bye, see you later",
	"nombreUs": "Set Username: ",
	"idUs": "Enter your id: ",
	"emailUs": "Enter your e-mail: ",
	"passwordUs": "Enter your password: ",
	"nombrePL": "Enter the Playlist name: ",
	"desPL": "Enter the description of the Playlist: "
	#El mismo comentario de arriba pero en inglés :v
	}
