import os
from Usuario import Usuario
from PlayList import Playlist
from Idiomas import Idioma
from Datos import Datos

#Esta clase es para ejecutar el programa

class Main:
    def __init__(self):
        self.break_while=1
        self.choices ={

                       "1": self.IniciarSesion,
                       "2": self.RegistrarUs,
                       "3": self.salir
        }
	
#Este método es para desplegar el menu
    
    @staticmethod
    def display_menu_login():
        print(Idioma.diccionarioMensajes.get("operacionesLogin"))

    @staticmethod    
    def display_menu_usuario():
        print(Idioma.diccionarioMensajes.get("operacionesUsuario"))
	
#Este método es para desplegar el menu

    @staticmethod
    def display_menu_admin():
        print(Idioma.diccionarioMensajes.get("operacionesAdmin"))

    @staticmethod
    def EliminarUs():
        if len(Usuario.lista_us)==0:
            print("No hay usuarios para eliminar.")
        else:
            while True:        
                idel=input((Idioma.diccionarioMensajes.get("ElId")))                
                if int(idel)<(len(Usuario.lista_us)):
                    Usuario.EliminarUs(idel)
                    break
                else:
                    print("El ID ingresado es inválido.")



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

    @staticmethod
    def IniciarSesion():
        while True:
            nombre=input((Idioma.diccionarioMensajes.get("nombreUs")))
            if Usuario.VerificacionNombre(nombre):
                pas=input(Idioma.diccionarioMensajes.get("passwordUs"))
            else:
                print('El usuario ingresado no está registrado.')        
        
    @staticmethod
    def RegistrarUs():
        while True:
            nombre=input((Idioma.diccionarioMensajes.get("nombreUs")))
            if Usuario.VerificacionNombre(nombre):
                print('El nombre de usuario ya está en uso.') 
            else:
                ema=input(Idioma.diccionarioMensajes.get("emailUs"))
                if Usuario.VerificacionEmail(ema):
                    print('El email ya se encuentra en uso.')
                else:
                    pas=input(Idioma.diccionarioMensajes.get("passwordUs"))
                    break    
        u1=Usuario(nombre,ema,pas)        
        Usuario.lista_us.append(u1) 		
        print(Idioma.diccionarioMensajes.get("saludo") + "" + u1.getNombre())

#Cambiar el nombre del usuario
 #remover el static y llamar el método desde la clase

#Crea Playlist
    @staticmethod
    def CrearPlaylist():
        nom=input(Idioma.diccionarioMensajes.get("nombrePL"))
        des=input(Idioma.diccionarioMensajes.get("desPL"))
        us=input(Idioma.diccionarioMensajes.get("nombreUsPlay"))
        p1=Playlist(nom,des,us)
        Playlist.lista_play.append(p1)
        print (Idioma.diccionarioMensajes.get("MensajeCreacionPlay"))


#Este método es para salir de la aplicación(? (No estoy muy seguro :c)
    @staticmethod
    def salir():
        print(Idioma.diccionarioMensajes.get("salir"))
        os._exit(0)

 

#Aqui se corre el programa
     
    def run (self):
        Main.idiomaMensajes()
        while self.break_while==1:
            self.display_menu_login()
            opcion = input(Idioma.diccionarioMensajes.get("opcion"))
            action = self.choices.get(opcion)
            if action:
                action()
            else:
                print(Idioma.diccionarioMensajes.get("opcionNoValida").format(opcion))
               
if __name__ == "__main__":
    Main().run()