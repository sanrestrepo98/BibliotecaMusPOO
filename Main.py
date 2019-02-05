import sys
from Usuario import Usuario
import PlayList
from Idiomas import Idioma

#Esta clase es para ejecutar el programa

class Main:

	def __init__(self):
		self.break_while=1
		self.choices ={
			"1": self.VerNombre,
        	"2": self.RegistrarUs,
       	 	"3": self.CambiarNombre,
       		"4": self.CrearPlaylist,
 			"5": self.salir
        }
	

#Este método es para desplegar el menu
	@staticmethod
	def display_menu():
		print(Idioma.diccionarioMensajes.get("operaciones"))

#Este método es para elegir el idioma
	@staticmethod
	def idiomaMensajes():
		print(""" Idioma:
			1. Español
			2. Ingles
			""")
		idioma = input("Seleccione un idioma: ")
		if idioma =="1":
			Idiomas.diccionarioMensajes = Idiomas.español
		elif idioma =="2":
			Idiomas.diccionarioMensajes = Idiomas.ingles

#Este método es para ver el nombre (creo que es obvio)

	def VerNombre(self):
		Usuario.getNombre()

#Este método es para ingresar usuarios

	def RegistrarUs (self):
		
		nombre=input("Ingrese nombre: ")
		
		num=int(input("Ingrese id: "))
		
		ema=input("Ingrese Email: ")
		
		pas=input("Ingrese contraseña: ")
		
		u1=Usuario(nombre,num,ema,pas)

		Usuario.lista_us.append(u1)
		
		print(u1.getNombre())

#Cambiar el nombre del usuario

	def CambiarNombre(self,nombre):
		Usuario.setNombre(nombre)

#Crea Playlist

	def CrearPlaylist(self):
		nom=input("Ingrese nombre de la Playlist")
		des=input("Ingrese descripcion de la Playlist")
		p1=Playlist(nom,des)
		Playlist.lista_play.append(p1)

#Este método es para salir de la aplicación(? (No estoy muy seguro :c)
	@staticmethod
	def salir():
		print(Idiomas.listaMensajes.get("salir"))
		sys._exit(0)
 

#Aqui se corre el programa
     
	def run (self):
		Main.idiomaMensajes()
		while self.break_while==1:
			self.display_menu()
			opcion = input(Idiomas.diccionarioMensajes.get("opcion"))
			action = self.choices.get(opcion)
			if action:
				action()
			else:
				print(Idiomas.diccionarioMensajes.get("opcionNoValida").format(opcion))
               
if __name__ == "__main__":
   Main().run()

