import sys
from Usuario import Usuario
from PlayList import Playlist
from Idiomas import Idioma

#Esta clase es para ejecutar el programa

class Main:
    def __init__(self):
        self.break_while=1
        self.choices ={
                       "1": self.RegistrarUs,
                       "2": self.CambiarNombre,
                       "3": self.verUsuarios,
                       "4": self.CrearPlaylist,
                       "5": self.salir
        }
	
#Este método es para desplegar el menu
    def verUsuarios(self):
       for usuario in Usuario.lista_us:
            print (usuario())

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

#Este método es para ingresar usuarios

    def RegistrarUs (self):
        nombre=input((Idioma.diccionarioMensajes.get("nombreUs")))
        num=input(Idioma.diccionarioMensajes.get("idUs"))
		
        ema=input(Idioma.diccionarioMensajes.get("emailUs"))
	
        pas=input(Idioma.diccionarioMensajes.get("passwordUs"))
        
        u1=Usuario(nombre,num,ema,pas)
        
        Usuario.lista_us.append(u1) 
		
        print(Idioma.diccionarioMensajes.get("saludo") + " " +u1.getNombre())

#Cambiar el nombre del usuario

    def CambiarNombre(self,nombre):
        Usuario.setNombre(nombre)

#Crea Playlist
    
    def CrearPlaylist(self):
        nom=input(Idioma.diccionarioMensajes.get("nombrePL"))
        des=input(Idioma.diccionarioMensajes.get("desPL"))
        p1=Playlist(nom,des)
        Playlist.lista_play.append(p1)

#Este método es para salir de la aplicación(? (No estoy muy seguro :c)
    @staticmethod
    def salir():
        print(Idioma.diccionarioMensajes.get("salir"))
        sys._exit(0)
 

#Aqui se corre el programa
     
    def run (self):
        Main.idiomaMensajes()
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