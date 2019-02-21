import os
from Usuario import Usuario
from PlayList import Playlist
from Idiomas import Idioma
from Datos import Datos


#Esta clase es para ejecutar el programa

class Main:
    
        
	
    @staticmethod
    def menuInicio():
        print(Idioma.diccionarioMensajes.get("operacionesInicio"))
        opcion=input(Idioma.diccionarioMensajes.get("opcion"))
        if opcion=="1":
            Main.IniciarSesion()
            Main.menuInicio()
        if opcion=="2":
            Main.RegistrarUs()
            Main.menuInicio()
        if opcion=="3":
            Main().run()
        if opcion=="4":            
            Main.salir()
        else:            
            print(Idioma.diccionarioMensajes.get("opcionNoValida").format(opcion))            
            Main.menuInicio()


#Este método es para desplegar el menu
    
    

    @staticmethod    
    def display_menu_usuario():
        print(Idioma.diccionarioMensajes.get("operacionesUsuario"))
	
#Este método es para desplegar el menu

    @staticmethod
    def display_menu_admin():
        print(Idioma.diccionarioMensajes.get("operacionesAdmin"))

   
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
        else:
            print(Idioma.diccionarioMensajes.get("opcionNoValida").format(idioma))
            Main.idiomaMensajes()


   

 
    @staticmethod
    def IniciarSesion():
        while True:
            nombre=input((Idioma.diccionarioMensajes.get("nombreUs")))
            if Usuario.VerificacionNombre(nombre):
                pas=input(Idioma.diccionarioMensajes.get("passwordUs"))
                if Usuario.Autenticacion(nombre,pas):
                    if Usuario.rolVer(nombre):
                        while True:
                            print(Usuario.display_menu_admin())
                            opcion = input(Idioma.diccionarioMensajes.get("opcion"))
                            if opcion=="5":
                                Main.menuInicio()
                            else:
                                Usuario.menuAdmin(str(opcion),nombre)
                    else:
                        sesion=True
                        while sesion:
                            print(Usuario.display_menu_usuario())
                            opcion = input(Idioma.diccionarioMensajes.get("opcion"))
                            if opcion=="4":
                                Main.menuInicio()
                            else:
                                Usuario.menu(str(opcion),nombre)                      
                else:
                    print(Idioma.diccionarioMensajes.get("credNo"))
            else:
                print(Idioma.diccionarioMensajes.get("NoReg"))   
       
        
    @staticmethod
    def RegistrarUs():        
        while True:
            nombre=input((Idioma.diccionarioMensajes.get("nombreUs")))
            if Usuario.VerificacionNombre(nombre):
                print(Idioma.diccionarioMensajes.get("UsExiste")) 
            else:
                ema=input(Idioma.diccionarioMensajes.get("emailUs"))
                if Usuario.VerificacionEmail(ema):
                    print(Idioma.diccionarioMensajes.get("EmExiste"))
                else:
                    pas=input(Idioma.diccionarioMensajes.get("passwordUs"))
                    break    
        u1=Usuario(nombre,ema,pas,"normal")        
        Usuario.lista_us.append(u1) 		
        print(Idioma.diccionarioMensajes.get("saludo") + "" + u1.getNombre())

#Cambiar el nombre del usuario


#Crea Playlist
    


#Este método es para salir de la aplicación(? (No estoy muy seguro :c)
    @staticmethod
    def salir():
        print(Idioma.diccionarioMensajes.get("salir"))
        os._exit(0)

 

#Aqui se corre el programa
     
    def run (self):
        Main.idiomaMensajes()        
        Main.menuInicio()
        
            
            
               
if __name__ == "__main__":
    Usuario.admin()
    Main().run()