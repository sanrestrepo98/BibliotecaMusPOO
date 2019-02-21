import sys
from Archivo import Archivo
from Idiomas import Idioma
class Playlist:

	lista_play=[]

	def __init__(self,nombreP,descripcion,usu,vis):
		self._nombreP=nombreP
		self._descripcion=descripcion
		self._listArc=[]
		self._us=usu
		self._vis=vis
		Playlist.lista_play.append(self)


#Agrega archivos
	def AgregarAr (self,nombreDeLaCan):
		for cancion in Archivo.ListaArchivos:
			if(cancion.getTitulo()==nombreDeLaCan):
				self._listArc.append(cancion)

	@staticmethod
	def CrearPlaylist(user):
		nom=input(Idioma.diccionarioMensajes.get("nombrePL"))
		des=input(Idioma.diccionarioMensajes.get("desPL"))
		while True:
			vis=input(Idioma.diccionarioMensajes.get("visPlay"))
			if vis=="0" or vis=="1":			
				Playlist(nom,des,user,vis)
				print(Idioma.diccionarioMensajes.get("MensajeCreacionPlay"))
				print(Idioma.diccionarioMensajes.get("crearPlayExito").format(nom))				
				break
			else:
				print(Idioma.diccionarioMensajes.get("opcionNoValida").format(vis))
        
	@staticmethod
	def verPlaylist():
		for play in Playlist.lista_play:
			print(play.getNombrep(),play.getDescripcion(),play.getUsu(),play.getVisi())

	@staticmethod
	def propPlay(usu):
		listaPropias=[]
		AuxIndi=0	
		for play in Playlist.lista_play:			
			if usu==play.getUsu():
				AuxIndi=1
				listaPropias.append(play)
				print(play.getNombrep(),play.getDescripcion())
				playli=int(input("Ingrese el ID de la playlist que desee: "))
				if playli<(len(listaPropias)):
					print(listaPropias[playli].getNombrep())

		if AuxIndi==0:
			print(Idioma.diccionarioMensajes.get("noPlay"))	

	@staticmethod
	def pubPlay():
		verif=0
		for play in Playlist.lista_play:
			if play.getVisi()=="1":
				verif=1
				print(play.getNombrep(),play.getDescripcion())
		if verif==0:
			print(Idioma.diccionarioMensajes.get("noPlay"))	



#Eliminar archivos
	@staticmethod
	def EliminarAr (nombreDeLaCancion):
		for titulo in Playlist.lista_play:
			if(titulo.getTitulo==nombreDeLaCancion):
				Playlist.lista_play.remove(titulo)

	@staticmethod
	def mostrarPlay():
		for play in Playlist.lista_play:
			print(play.verPlay())

	

#Gets y sets para nombre de la playlist y la descripcion

	def getVisi(self):
		return self._vis

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