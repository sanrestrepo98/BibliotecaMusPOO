import sys
class Usuario:

	lista_us=[]

	def __init__(self,nombre,id,email,password):
		self._nombre=nombre
		self._id=id
		self._email=email
		self._password=password
		Usuario.lista_us.append(self)

##Este método elimina usuarios
	@staticmethod
	def EliminarUs (self,id):
		for ids in Usuario.getId():
			if(id==ids):
				Usuario.lista_us.remove(ids)

#Los gets y sets para id, nombre, email, pero solo en password tiene set
	def getId (self):
		return self._id

	def setId (self,id):
		self._id=id

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





