import sys
class Usuario:

	lista_us=[]

	def __init__(self,nombre,ids,email,password):
		self._nombre=nombre
		self._ids=ids
		self._email=email
		self._password=password
		Usuario().lista_us.append(self)

##Este método elimina usuarios
	@staticmethod
	def EliminarUs (self,ids):
		for idss in Usuario.lista_us():
			if(ids==idss.getId()):
				Usuario().lista_us.remove(idss)

#Los gets y sets para id, nombre, email, pero solo en password tiene set
	def getId (self):
		return self._id

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





