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





