import sys
from Idiomas import Idioma
class Usuario:
	_id=0
	lista_us=[]

	def __init__(self,nombre,email,password):
		self._nombre=nombre

		Usuario._id+=1
		self._id=Usuario._id

		self._email=email
		self._password=password
		self._listaResenas=[]
		self._playlisty=[]
		Usuario.lista_us.append(self)
		

##Este método elimina usuarios
	@staticmethod
	def mostrarUsuarios():
		for arc in Usuario.lista_us:
			print (arc.verUsuarios())
	@staticmethod
	def EliminarUs (id):
		for ids in Usuario.lista_us:
			if(id==ids.getId()):
				Usuario.lista_us.remove(ids)

#Los gets y sets para id, nombre, email, pero solo en password tiene set
	def setResena(self, comment):
		self._listaResenas.append(comment)

	def EliminarUs (self,ids):
		Usuario.lista_us.pop(int(ids))
		print('Total de usuarios:'+" "+str(len(Usuario.lista_us)))

	@staticmethod
	def verUsuarios():
	    for usuario in Usuario.lista_us:
	        print(usuario._nombre,usuario._email,usuario._password)

		

	@staticmethod
	def VerificacionNombre(nombre):
		for usuario in Usuario.lista_us:
			if nombre==usuario._nombre:
				return True
	
	@staticmethod
	def VerificacionEmail(email):
		for usuario in Usuario.lista_us:
			if email==usuario._email:
				return True

#Los gets y sets para id, nombre, email, pero solo en password tiene set
	def getId (self):
		return self._ids

	def setPlaylist(self,play):
		self._playlisty.append(play)

	def getPlaylist(self):
		return self._playlisty

	def getId(self):
		return self._id

	def getNombre(self):
		return self._nombre

	@staticmethod
	def setNombre(nom):
		self._nombre=nom

	def getEmail(self):
		return self._email

	def setEmail(self,email):
		self._email=email

	def setPassword(self,password):
		self._password=password

	def verUsuarios(self):
		retorno = Idioma.diccionarioMensajes.get("formatoUsuario") % (self.getId(),self.getNombre(),self.getEmail())
		for play in self.getPlaylist():
			retorno = retorno +" \n" +play.verPlayinRef() 
		return retorno
