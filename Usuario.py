import os
from Idiomas import Idioma
from PlayList import Playlist

class Usuario:
	lista_us=[]
	
	def __init__(self,nombre,email,password,rol):
		self._nombre=nombre
		self._email=email
		self._password=password
		self._rol=rol
		self._listaResenas=[]
		self._playlisty=[]
		

	#Inicializador del admin	
	@staticmethod
	def admin():
		u=Usuario("admin","admin","123","admin")
		Usuario.lista_us.append(u)
		print(len(Usuario.lista_us))


##Este método elimina usuarios
	@staticmethod
	def EliminarUs():
		if len(Usuario.lista_us)==0:
			print(Idioma.diccionarioMensajes.get("NoUsuElim"))
		else:
			while True:
				idel=input((Idioma.diccionarioMensajes.get("ElId")))
				if int(idel)<(len(Usuario.lista_us)):
					Usuario.lista_us.pop(int(idel))
					print('Total de usuarios:'+" "+str(len(Usuario.lista_us)))
					break
				else:
					print(Idioma.diccionarioMensajes.get("NoUsuElim"))

#Los gets y sets para id, nombre, email, pero solo en password tiene set
	def setResena(self, comment):
		self._listaResenas.append(comment)
		
	@staticmethod
	def display_menu_usuario():
		return Idioma.diccionarioMensajes.get("operacionesUsuario")
		
	@staticmethod
	def menu(opcion,user):
		if opcion=="1":
			Usuario.CrearPlaylist(user)
		elif opcion=="3":
			Usuario.salir()
		else:
			print(Idioma.diccionarioMensajes.get("opcionNoValida").format(opcion))
		 

	@staticmethod
	def display_menu_admin():
		return Idioma.diccionarioMensajes.get("operacionesAdmin")
		
	
	@staticmethod
	def menuAdmin(opcion,user):
		if opcion=="1":			
			Usuario.EliminarUs()
		elif opcion=="2":
			#Usuario.setNombre
			print("op 2 imp")
		elif opcion=="3":
			Usuario.verUsuarios()			
		elif opcion=="5":
			Usuario.salir()
		else:
			print(Idioma.diccionarioMensajes.get("opcionNoValida").format(opcion))
		
	
	@staticmethod
	def CrearPlaylist(user):
		nom=input(Idioma.diccionarioMensajes.get("nombrePL"))
		des=input(Idioma.diccionarioMensajes.get("desPL"))
		p1=Playlist(nom,des,user)
		Playlist.lista_play.append(p1)
		print(nom,des,user)
		print(Idioma.diccionarioMensajes.get("MensajeCreacionPlay"))
        

	@staticmethod
	def verUsuarios():
	    for usuario in Usuario.lista_us:
	        print(usuario._nombre,usuario._email,usuario._password)
		

	@staticmethod
	def VerificacionNombre(nombre):
		for usuario in Usuario.lista_us:
			if nombre==usuario.getNombre():
				return True
	
	@staticmethod
	def VerificacionEmail(email):
		for usuario in Usuario.lista_us:
			if email==usuario.getEmail():
				return True

	@staticmethod
	def Autenticacion(nombre,pas):
		for usuario in Usuario.lista_us:
			if nombre==usuario.getNombre():
				if pas==usuario._password:					
					return True

	@staticmethod
	def rolVer(nombre):
		for usuario in Usuario.lista_us:
			if nombre==usuario.getNombre():
				if "admin"==usuario.getRol():
					return True
	
	@staticmethod
	def obtenerId(user):
		for usuario in Usuario.lista_us:
			if user==usuario.getNombre():
				id=Usuario.lista_us.index(user)
				return id
		

#Los gets y sets para id, nombre, email, pero solo en password tiene set


	def setPlaylist(self,play):
		self._playlisty.append(play)

	def getPlaylist(self):
		return self._playlisty

	def getNombre(self):
		return self._nombre

	def getRol(self):
		return self._rol

	def setNombre(self,nom):
		self._nombre=nom

	def getEmail(self):
		return self._email

	def setEmail(self,email):
		self._email=email

	def setPassword(self,password):
		self._password=password


	@staticmethod
	def salir():
		print(Idioma.diccionarioMensajes.get("salir"))
		os._exit(0)
