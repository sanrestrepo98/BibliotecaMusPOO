import sys
import Archivo
import Usuario
class Reporte:
	
	ListaReportes = {}

	def __init__ (self,fecha,descripcion):
		date self._fecha=fecha
		str self._descripcion=descripcion
		Reporte.ListaReportes.append()

	def setFecha (self,fecha):
		self._fecha = fecha

	def getFecha (self):
		return self._fecha

	def setDescripcion (self,descripcion):
		self._descripcion

	def getDescripcion (self,descripcion):
		self._descripcion