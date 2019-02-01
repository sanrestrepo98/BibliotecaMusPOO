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
	def BuscarPorTitulo(self,title):
		for song in Archivo.ListaArchivos:
			if Archivo.getTitulo() == title:
				return song

	@staticmethod
	def BuscarPorArtista(self,artista):
		for song in Archivo.ListaArchivos:
			if Archivo.getArtista() == artista:
				return song

	@staticmethod
	def BuscarPorAlbum(self,album):
		for song in Archivo.ListaArchivos:
			if Archivo.getAlbum() == album:
				return song

	@staticmethod
	def BuscarPorGenero(self,genero):
		for song in Archivo.ListaArchivos:
			if Archivo.getGenero() == genero:
				return song

	@staticmethod
	def BuscarPorRegion(self,region):
		for song in Archivo.ListaArchivos:
			if Archivo.getRegion() == genero:
				return song

	@staticmethod
	def BorrarArchivo(self,titulo):
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
		return self._Album

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

if __name__ == "__main__":
print (Archivo())