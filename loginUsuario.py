import os
from Idiomas import Idioma

class loginUsuario:
    def __init__(self):
        self.break_while=1
        self.choices ={
                       "1": self.CrearPlaylist,
                       "2": self.salir                     
        }

    @staticmethod
    def display_menu_usuario():
         return Idioma.diccionarioMensajes.get("operacionesUsuario")

    @staticmethod
    def CrearPlaylist():
        print("pirulí")

    @staticmethod
    def salir():
        print(Idioma.diccionarioMensajes.get("salir"))
        os._exit(0)