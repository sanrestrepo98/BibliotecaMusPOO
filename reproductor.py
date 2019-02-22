import pygame
import time
import os 
import shutil
def eleccion():
    list=[]
    print("elige la opcion ")
    path="C:/Users/user/Documents/GitHub/BibliotecaMusPOO/biblioteca"
    dirs = os.listdir( path )
    for i in range(len(dirs)):
        print(i,dirs[i])
    
    opcion=input("opcion")
    x=int(opcion)
    m=dirs[x]
    aux=path+"/"+m
    print(aux)
    reproducir(aux)
    
    reprodutor()
def reproducir(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(5)
    reprodutor()
def pause():
	pygame.mixer.music.pause()
	reprodutor()
def stop():
	pygame.mixer.music.stop()
	reprodutor()
def salir():
    os._exit(0)
def biblioteca():
	os.mkdir("biblioteca")
	time.sleep(5)
def agregar():
   aux=input("ingrese la direcion del archivo")
   x=shutil.copy(aux, (input("nombre")+".mp3"))
   shutil.move(x,"biblioteca")
def reprodutor():
    print("elige la opcion ")
    print("1.reproducir")
    print("2.pause")
    print("3.stop")
    print("4.salir")	
    opcion=input("opcion")
    if opcion=="1":
        eleccion()   
    if opcion=="2":
        pause()   
    if opcion=="3":
        stop()   
    if opcion=="4":            
        salir()
    else:
        reprodutor()
reprodutor()
#biblioteca()	
#caso()
     #

