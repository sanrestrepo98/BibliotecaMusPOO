import sys
class Usuario:

	lista_us=[]

	def __init__(self,nombre,email,password):
		self._nombre=nombre
		self._email=email
		self._password=password
		Usuario.lista_us.append(self)
		

##Este método elimina usuarios
	@staticmethod
	def EliminarUs (ids):
		Usuario.lista_us.remove(ids)

	@staticmethod
	def verUsuarios():
	   for usuario in Usuario.lista_us:
	           print(usuario._nombre)

#Los gets y sets para id, nombre, email, pero solo en password tiene set
	def getId (self):
		return self._ids

	def setId (self,ids):
		self._ids=ids

	def getNombre(self):
		return self._nombre

	def setNombre(self,nombre):
		self._nombre=nombre

	def getEmail(self):
		return self._email

	def setEmail(self,email):
		self._email=email

	def setPassword(self,password):
		self._password=password





