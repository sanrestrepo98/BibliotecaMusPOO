from Usuario import Usuario
import random as r
from PlayList import Playlist
class Datos:

	usuarios = []
	email = []
	contraseña= []
	rol=[]
	Play=[]
	descripcion=[]
	visibilidad=[]
	def leer_archivos():

    with open('usuarios.txt') as data_file: 
        for line in data_file: 
           usuarios.append(line.strip().split(',')) 
    with open('email.txt') as data_file: 
        for line in data_file: 
           email.append(line.strip().split(',')) 
    with open('contraseña.txt') as data_file: 
        for line in data_file: 
           contraseña.append(line.strip().split(',')) 
    with open('rol.txt') as data_file: 
        for line in data_file: 
           rol.append(line.strip().split(',')) 
    with open('Play.txt') as data_file: 
        for line in data_file: 
           Play.append(line.strip().split(',')) 
    with open('descripcion.txt') as data_file: 
        for line in data_file: 
           descripcion.append(line.strip().split(',')) 
    with open('visibilidad.txt') as data_file: 
        for line in data_file: 
           visibilidad.append(line.strip().split(',')) 
	@staticmethod
	def generarUsuarios():
		leer_archivos()
		for i in range (0,len(Datos.usuarios)):
			nom = Datos.usuarios[i]
			ema = Datos.email[i]
			pas = Datos.contraseña[i]
			rol= Datos.rol[i]
			us=Usuario(nom,ema,pas,rol)
			Usuario.lista_us.append(us)

	@staticmethod
	def generarPaly():
		for i in range (0,len(Datos.Play)):
			nombre = Datos.Play[i]
			des = Datos.descripcion[i]
			usu = r.choice(Usuario.lista_us)
			vis= Datos.visibilidad[i]
			p=Playlist(nombre,des,usu,vis)
			Playlist.lista_play.append(p)