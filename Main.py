import sys
import Usuario
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
			Idioma.diccionarioMensajes = Idioma.español
		elif idioma =="2":
			Idioma.diccionarioMensajes = Idioma.ingles

#Este método es para ver el nombre (creo que es obvio)

	def VerNombre(self):
		Usuario().getNombre()

#Este método es para ingresar usuarios

	def RegistrarUs (self):
		u1=Usuario()
		nombre=input("Ingrese nombre: ")
		u1.setNombre(nombre)
		num=int(input("Ingrese id: "))
		u1.setId(num)
		ema=input("Ingrese Email: ")
		u1.setEmail(ema)
		pas=input("Ingrese contraseña: ")
		u1.setPassword(pas)
		Usuario.lista_us.append(u1)

#Cambiar el nombre del usuario

	def CambiarNombre(self,nombre):
		Usuario().setNombre(nombre)

#Crea Playlist

	def CrearPlaylist(self):
		p1=Playlist()
		nom=input("Ingrese nombre de la Playlist")
		p1.setNombreP(nom)
		des=input("Ingrese descripcion de la Playlist")
		p1.setDescripcion(des)
		Playlist().lista_play.append(p1)

#Este método es para salir de la aplicación(? (No estoy muy seguro :c)
	@staticmethod
	def salir():
		print(Idioma.listaMensajes.get("salir"))
		sys._exit(0)
 

#Aqui se corre el programa
     
	def run (self):
		while self.break_while==1:
			self.display_menu()
			opcion = input(Idioma.diccionarioMensajes.get("opcion"))
			action = self.choices.get(opcion)
			if action:
				action()
			else:
				print(Idioma.diccionarioMensajes.get("opcionNoValida").format(opcion))
               
if __name__ == "__main__":
   Main().run()



