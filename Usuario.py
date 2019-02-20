import os
from Idiomas import Idioma
from PlayList import Playlist

class Usuario:
	lista_us=[]

	def __init__(self,nombre,email,password):
		self._nombre=nombre
		self._email=email
		self._password=password
		self._listaResenas=[]
		self._playlisty=[]
		Usuario.lista_us.append(self)
		

	

##Este método elimina usuarios
	@staticmethod
	def EliminarUs (ids):
		Usuario.lista_us.pop(int(ids))
		print('Total de usuarios:'+" "+str(len(Usuario.lista_us)))

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
		if opcion=="3":
			Usuario.salir()
	
	@staticmethod
	def CrearPlaylist(user):
		nom=input(Idioma.diccionarioMensajes.get("nombrePL"))
		des=input(Idioma.diccionarioMensajes.get("desPL"))
		p1=Playlist(nom,des,user)
        #Playlist.lista_play.append(p1)
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

#Los gets y sets para id, nombre, email, pero solo en password tiene set


	def setPlaylist(self,play):
		self._playlisty.append(play)

	def getPlaylist(self):
		return self._playlisty

	def getNombre(self):
		return self._nombre

	
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
