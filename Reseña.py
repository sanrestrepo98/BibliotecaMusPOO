import sys
class Reseña:

	ListaReseñas = {}

	def __init__(self,fecha,calificacion,comentario):
		date self._fecha=fecha
		self._calificacion=calificacion
		self._comentario=comentario
		Reseña.ListaReseñas.append(self)

	def setFecha (self,fecha):
		self._fecha = fecha

	def getFecha (self):
		return self._fecha

	def setCalificacion (self,calificacion):
		self._calificacion=calificacion

	def getCalificacion (self):
		return self._calificacion
		