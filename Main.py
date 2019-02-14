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
<<<<<<< HEAD
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
=======
                       "1": self.RegistrarUs,
                       "2": self.CambiarNombre,
                       "3": self.verUsuarios,
                       "4": self.CrearPlaylist,
<<<<<<< HEAD
                       "5": self.VerPlay,
                       "6": self.GenerarUsuarios,
                       "7": self.GenerarPlay,
                       "8": self.salir
        }
	
#Este método es para desplegar el menu
    def verUsuario(self):
        Usuario.mostrarUsuarios()

    def VerPlay(self):
        Playlist.mostrarPlay()

    def GenerarUsuarios(self):
        Datos.generarUsuarios()

    def GenerarPlay(self):
        Datos.generarPaly()
=======
                       "5": self.EliminarUs,
                       "6": self.salir
        }
	
#Este método es para desplegar el menu
>>>>>>> 21f6b96a209c5d4f6b31b6e8bce4f82c2c90e6ee
>>>>>>> be9d3101b97d9b526f59d02fe7129537e8e034a3

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
<<<<<<< HEAD
    def RegistrarUs ():
        nombre=input((Idioma.diccionarioMensajes.get("nombreUs")))
		
        ema=input(Idioma.diccionarioMensajes.get("emailUs"))
	
        pas=input(Idioma.diccionarioMensajes.get("passwordUs"))
        
        u1=Usuario(nombre,ema,pas)
        
        Usuario.lista_us.append(u1) 
		
        print(Idioma.diccionarioMensajes.get("saludo") + "" + u1.getNombre())
=======
    def verUsuarios():
        Usuario.verUsuarios()

    @staticmethod
    def IniciarSesion():
        while True:
            nombre=input((Idioma.diccionarioMensajes.get("nombreUs")))
            if Usuario.VerificacionNombre(nombre):
                break
            else:
                print('El usuario ingresado no está registrado.')        
        while True:
            pas=input(Idioma.diccionarioMensajes.get("passwordUs"))
            if Usuario.VerificacionEmail(email):
                print('El email ya se encuentra en uso.')
            else:
                break



    @staticmethod
    def RegistrarUs ():        
        while True:
            nombre=input((Idioma.diccionarioMensajes.get("nombreUs")))
            if Usuario.VerificacionNombre(nombre):
                print('El nombre ya se encuentra ocupado.')
            else:
                break
        
        while True:
            email=input(Idioma.diccionarioMensajes.get("emailUs"))
            if Usuario.VerificacionEmail(email):
                print('El email ya se encuentra en uso.')
            else:
                break
        pas=input(Idioma.diccionarioMensajes.get("passwordUs"))        
        Usuario(nombre,email,pas)    
        print(Idioma.diccionarioMensajes.get("saludo") + " " +nombre)
>>>>>>> 21f6b96a209c5d4f6b31b6e8bce4f82c2c90e6ee

#Cambiar el nombre del usuario
    @staticmethod
    def CambiarNombre(n):
        Usuario.setNombre(n)

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
    
    def salir():
        print(Idioma.diccionarioMensajes.get("salir"))
<<<<<<< HEAD
        sys.exit(0)
=======
        os._exit(0)
>>>>>>> 21f6b96a209c5d4f6b31b6e8bce4f82c2c90e6ee
 

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