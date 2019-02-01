import sys
class Playlist:

	lista_play=[]

	def __init__(self,nombreP,descripcion):
		self._nombreP=nombreP
		self._descripcion=descripcion
		Playlist.lista_play.append(self)

#Agrega archivos
	@staticmethod
	def AgregarAr(self,nombreDeLaCancion):
		for titulo in Archivo.getTitulo():
			if(titulo==nombreDeLaCancion):
				Playlist.lista_play.append(Archivo.getTitulo)

#Eliminar archivos
	@staticmethod
	def EliminarAr(self,nombreDeLaCancion):
		for titulo in Archivo.getTitulo():
			if(titulo==nombreDeLaCancion):
				Playlist.lista_play.remove(Archivo.getAudio)

#Gets y sets para nombre de la playlist y la descripcion
	def setNombreP(self,nombreP):
		self._nombreP=nombreP

	def getNombre(self):
		return self._nombreP

	def setDescripcion(self,descripcion):
		self._descripcion=descripcion

	def getDescripcion(self):
		return self._descripcion
		