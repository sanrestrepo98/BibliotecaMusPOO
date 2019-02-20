import sys
from Archivo import Archivo
from Idiomas import Idioma
class Playlist:

	lista_play=[]

	def __init__(self,nombreP,descripcion,usu):
		self._nombreP=nombreP
		self._descripcion=descripcion
		self._listArc=[]
		self._us=usu
		Playlist.lista_play.append(self)

#Agrega archivos
	@staticmethod
	def AgregarAr (self,nombreDeLaCan):
		for cancion in Archivo.ListaArchivos:
			if(cancion.getTitulo()==nombreDeLaCan):
				PlayList.setArc(cancion)

#Eliminar archivos
	@staticmethod
	def EliminarAr (self,nombreDeLaCancion):
		for titulo in Playlist.lista_play:
			if(titulo.getTitulo==nombreDeLaCancion):
				Playlist.lista_play.remove(titulo)

	@staticmethod
	def mostrarPlay():
		for play in Playlist.lista_play:
			print(play.verPlay())

	

#Gets y sets para nombre de la playlist y la descripcion

	def setArc(self, arc):
		self._listArc.append(arc)

	def getArc(self):
		return self._listArc

	def setUsu(self, us):
		self._us=us
		us.setPlaylist(self)

	def getUsu(self):
		return self._us

	def setNombreP(self,nombreP):
		self._nombreP=nombreP

	def getNombrep(self):
		return self._nombreP

	def setDescripcion(self,descripcion):
		self._descripcion=descripcion

	def getDescripcion(self):
		return self._descripcion
		
	def verPlay(self):
		retorno = Idioma.diccionarioMensajes.get("formatoPlay") % (self.getNombrep(), self.getDescripcion(), self.getUsu().getNombre())
		return retorno

	def verPlayinRef(self):
		retorno = Idioma.diccionarioMensajes.get("formatoCortoPlay") % (self.getNombrep(), self.getDescripcion())
		return retorno