from Idiomas import Idioma
from Main import Main

class loginUsuario:
    def __init__(self):
        self.break_while=1
        self.choices ={
                       "1": self.CrearPlaylist,
                       "2": Main.salir                     
        }

        def display_menu_usuario():
            print(Idioma.diccionarioMensajes.get("operacionesUsuario"))