import sys
import Archivo
from Usuario import Usuario
class Reporte:
	
	ListaReportes = []

	def __init__ (self,fecha,descripcion):
		self._fecha=fecha
		self._descripcion=descripcion
		Reporte.ListaReportes.append(self)

	def setFecha (self,fecha):
		self._fecha = fecha

	def getFecha (self):
		return self._fecha

	def setDescripcion (self,descripcion):
		self._descripcion

	def getDescripcion (self,descripcion):
		self._descripcion