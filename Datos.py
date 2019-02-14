from Usuario import Usuario
import random as r
from PlayList import Playlist
class Datos:

	usuarios = ["Manuel","David","Santiago","Esteban","Nazly","Camu","euin"]
	email = ["man@unal","davi@unal","salti@unal","esteba@unal","nazly@unal","cam@unal", "euin@unal" ]
	contraseña= ["asdw","asdf","asdf4r2", "asdfqwer","sdfgwer","aerqw445","wytuiyiyt6"]
	Play=["lamejor","bailar","caminar","matar","enterrar","fingir","culQ#$%",]
	descripcion=["cuando este feliz","para conocer la victima","cuando ya me tenga confianza","bueno, mas felicidad","cuando me interroguen","visitar el cuerpo todas las noches"]
		
	@staticmethod
	def generarUsuarios():
		for i in range (0,len(Datos.usuarios)):
			nom = Datos.usuarios[i]
			ema = Datos.email[i]
			pas = Datos.contraseña[i]
			us=Usuario(nom, ema, pas)
			Usuario.lista_us.append(us)

	@staticmethod
	def generarPaly():
		for i in range (0,len(Datos.Play)):
			nombre = Datos.Play[i]
			des = Datos.descripcion[i]
			usu = r.choice(Usuario.lista_us)
			p=Playlist(nombre,des,usu)
			Playlist.lista_play.append(p)