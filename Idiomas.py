import sys
class Idioma:
	diccionarioMensajes = {}
	#Acá van todos los mensajes en español, tenemos que definir cuáles serán, por el momento pondré el menú inicial
	español = {
	"operacionesLogin": """
		Opciones
		1. Iniciar Sesión
		2. Registrarse	
		3. Salir
		""",
	"operacionesUsuario": """
		Opciones
		1. Crear Playlist
		2. Salir
		""",
	"operacionesAdmin": """
		Opciones
		1. Eliminar Usuario
		2. Cambiar Nombre
		3. Ver Usuarios
<<<<<<< HEAD
		4. Salir
=======
		4. Crear Playlist
		5. ver Playlist
		6. Generar Usuarios
		7. Generar Playlist(genere usuarios primero)
		8. Salir		
>>>>>>> be9d3101b97d9b526f59d02fe7129537e8e034a3
		""",

      "saludo": "Hola ",
	"opcion": "¿Qué desea hacer?: ",
	"opcionNoValida": "{0} no es una opción válida",
	"salir": "Hasta luego, vuelve pronto :c",
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
	"MensajeCreacionPlay": "Has creado una PlayList :3",
	"desPL": "Ingrese la descripción de la Playlist: ",
	"ElId": "Ingrese el id del usuario a eliminar: ",
	#Acá se van agregando todos los textos que querramos
	}
	
	ingles = {
	"operaciones": """
		Options
		1. Sign up
		2. Rename
		3. See user
		4. Create Playlist
		5. See Playlist
		6. Generate Users
		7. Generate Playlist
		6. Exit
		""",
      "saludo": "Hi ",
	"opcion": "What would you like to do?: ",
	"opcionNoValida": "{0} isn't a valid option",
	"salir": "Bye, see you later",
	"nombreUs": "Set Username: ",
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
