import os
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
                       "5": self.EliminarUs,
                       "6": self.salir
        }
	
#Este método es para desplegar el menu

    @staticmethod
    def display_menu():
        print(Idioma.diccionarioMensajes.get("operaciones"))

    @staticmethod
    def EliminarUs():
        idel=input((Idioma.diccionarioMensajes.get("ElId")))
        Usuario.EliminarUs(idel)

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

    @staticmethod
    def verUsuarios():
        Usuario.verUsuarios()

#Este método es para ingresar usuarios
    @staticmethod
    def RegistrarUs ():
        x=True
        while x:
            nombre=input((Idioma.diccionarioMensajes.get("nombreUs")))
            if Usuario.VerificacionNombre(nombre):
                print('El nombre ya se encuentra ocupado.')
            else:
                nam=nombre
                x=False
        x=True
        while x:
            email=input(Idioma.diccionarioMensajes.get("emailUs"))
            if Usuario.VerificacionEmail(email):
                print('El email ya se encuentra en uso.')
            else:
                ema=email
                x=False 	
        pas=input(Idioma.diccionarioMensajes.get("passwordUs"))        
        Usuario(nam,ema,pas)    
        print(Idioma.diccionarioMensajes.get("saludo") + " " +nombre)

#Cambiar el nombre del usuario
    @staticmethod
    def CambiarNombre(nombre):
        Usuario.setNombre(nombre)

#Crea Playlist
    @staticmethod
    def CrearPlaylist():
        nom=input(Idioma.diccionarioMensajes.get("nombrePL"))
        des=input(Idioma.diccionarioMensajes.get("desPL"))
        p1=Playlist(nom,des)
        Playlist.lista_play.append(p1)

#Este método es para salir de la aplicación(? (No estoy muy seguro :c)
    @staticmethod
    def salir():
        print(Idioma.diccionarioMensajes.get("salir"))
        os._exit(0)
 

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