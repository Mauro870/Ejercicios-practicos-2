import requests 
import socket

class solicitud:
    def __init__(self,URL):
        self.__ip=socket.gethostbyname(URL)
        self.__URL11=  "https://"+ URL
        self.__URL1 = requests.get(url = self.__URL11)
        self.__Server = self.__URL1.headers.setdefault('Server','None')
        self.__ConEn = self.__URL1.headers.setdefault('Content-Encoding','None')
        self.__Condi = self.__URL1.encoding
        
    def Mostrar(self):
        print("IP: ",self.__ip)
        print("Servidor: ",self.__Server)
        print("Tipo de contenido: ",self.__ConEn)
        print("Codificaciòn: ",self.__Condi)
sitios= ["www.google.com","www.udea.edu.co","www.itm.edu.co","www.elcolombiano.com"]        
for sitio in sitios:
    Datos = solicitud(sitio)
    Datos.Mostrar()
    print('')
