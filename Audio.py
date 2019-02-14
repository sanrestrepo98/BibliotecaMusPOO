import sys
class Archivo:
	
	ListaArchivos = []
	
	def __init__ (self, titulo,artista,album,genero,region,fecha):
		self._titulo=titulo
		self._artista=artista
		self._album=album
		self._genero=genero
		self._region=region
		self._descargas=0
		self._fecha=fecha
		Archivo.ListaArchivos.append(self)

	@staticmethod
	def BuscarPorTitulo(title):
		for song in Archivo.ListaArchivos:
			if song.getTitulo() == title:
				return song

	@staticmethod
	def BuscarPorArtista(artista):
		for song in Archivo.ListaArchivos:
			if song.getArtista() == artista:
				return song

	@staticmethod
	def BuscarPorAlbum(album):
		for song in Archivo.ListaArchivos:
			if song.getAlbum() == album:
				return song

	@staticmethod
	def BuscarPorGenero(genero):
		for song in Archivo.ListaArchivos:
			if song.getGenero() == genero:
				return song

	@staticmethod
	def BuscarPorRegion(region):
		for song in Archivo.ListaArchivos:
			if song.getRegion() == region:
				return song

	@staticmethod
	def BorrarArchivo(titulo):
		Archivo.ListaArchivos.remove(titulo)

	def setTitulo (self, title):
		self._titulo = title

	def getTitulo (self):
		return self._titulo

	def setArtista (self,artista):
		self._artista = artista

	def getArtista (self):
		return self._artista

	def setAlbum (self,album):
		self._album = album

	def getAlbum (self):
		return self._album

	def setGenero (self,genero):
		self._genero = genero

	def getGenero (self):
		return self._genero

	def setRegion (self,region):
		self._region = region

	def getRegion (self):
		return self._region

	def setDescargas (self,descargas):
		self._descargas = descargas

	def getDescargas (self):
		return self._descargas

	def setFecha (self,fecha):
		self._fecha = fecha

	def getFecha (self):
		return self._fecha