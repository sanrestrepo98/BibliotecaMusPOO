import Usuario
import PlayList
import sys

#Esta clase es para ejecutar el programa

class Main:


	def __init__(self):
		self.break_while=1
		self._choises ={
		'1': self._Ver_nombre,
        '2': self._Ingresar_usuario,
        '3': self._Cambiar_nombre,
        '4': self._Crear_play,
        '5': self._salir,
        }

#Este método es para desplegar el menu

	def display_menu(self):
		print("""
        Operaciones
        1. Ver nombre
        2. Registrar usuario
        3. Cambiar nombre
        4. Crear Playlist
        5. Salir
        """)

#Este método es para ver el nombre (creo que es obvio)

	def VerNombre(self):
		Usuario.getNombre()

#Este método es para ingresar usuarios

	def IngresarUs (self):
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
		Usuario.setNombre(nombre)

#Crea Playlist

	def CrearPlaylist(self):
		p1=Playlist()
		nom=input("Ingrese nombre de la Playlist")
		p1.setNombreP(nom)
		des=input("Ingrese descripcion de la Playlist")
		p1.setDescripcion(des)
		Playlist.lista_play.append(p1)


	def salir (self):
		print("Hasta luego")
		sys.exit(0)
 

#Aqui se corre el programa
     
	def run (self):
		while self.break_while==1:
			self.display_menu()
			opcion = input("Ingrese una opcion: ")
			action = self.choices.get(opcion)
			if action:
				action()
			else:
				print("{0} no es una opcion valida".format(opcion))
               
if __name__ == "__main__":
  
   Main.run()



