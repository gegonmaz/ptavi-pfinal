#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un cliente-servidor
"""

""" 
Agente del servidor
"""

import socket
import sys
import csv
import urllib.request
import json
import time
import logging
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


# Tendremos que tener una variable donde se guarde el XML
FicheroXML = sys.argv[1]
# El metodo que se va a ejecutar
Metodo = sys.argv[2]
# Dependiendo del metodo, tendremos una opcion diferente
if Metodo == REGISTER
    TiempoExpiracion = sys.argv[3]
elif Metodo == INVITE
    Usuario = sys.argv[3]
else Metodo == BYE
    UsuarioDesconectado = sys.argv[3]
# Creamos las variables de forma global para poder utilizarlas durante el prog.

class UAClientHandler(ContentHandler):

"""
User Agent del cliente
"""

    """
    Vamos a crear una funcion que se encargue de crear un diccionario con 
    las etiquetas del archivo XML para ir guardando los datos.
    """

    def __init__(self):

        self.listaEtiquetas = []
        self.diccionarioConfig = {'account': ['username', 'password'],
                                  'uaserver': ['ip', 'puerto'],
                                  'rtpaudio': ['puerto'],
                                  'regproxy': ['ip', 'puerto'],
                                  'log': ['path'],
                                  'audio': ['path']}

    """
    Vamos a tener que inicializar todos los elementos(etiquetas) del 
    diccionario creado anteriormente
    """
    def InicializacionElementos(self,name,attrs):
        # Buscaremos las etiquetas en el diccionario
        if name in self.diccionarioConfig:
            Valores = {}
            for etiquetas in self.diccionarioConfig[name]:
                Valores[name] = attrs.get(etiquetas, '')
            listaNombres = {name: Valores}
            self.listaEtiquetas.append(listaNombres)


    def get_tags(self):
        # Nos tendrá que devolver la lista segun como este
        return self.listaEtiquetas

    """
    Tendremos que crear un archivo log; de modo que si cae el servicio,
    se pueda saber que usuarios estaban contectados en cada momento
    """
    def archivoLog(File, Message)
        # Primero aseguramos si existe algún fichero ya
        ficheroLectura = open(File, 'r')
        lineas = fichero.readlines
        ficheroLectura.close()
        lineas.append(str(time.time()) + '' + Message)
        # Escribimos en el fichero
        ficheroEscritura = open(File, 'w')
        ficheroEscritura(''.join(lienas))
        ficheroEscritura.close()    

    """
    Una vez inicializadas, tendremos que crear alguna funcion que nos permita
    acceder a las etiquetas
    """
    parser =make_parser()
    cHandler = UAClientHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(FicheroXML)


if __name__ == "__main__":

    # Tendremos que crear el socket 
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    # Esta vez en vez de anudarlo a un servidor, lo haremos al Proxy
    my_socket.connect((diccionarioConfig['regproxy']['ip'], 
                       int(diccionarioConfig['regproxy']['puerto']))

    # El programa tendrá que actuar segun el metodo que haya recibido
    
    if len(sys.argv) != 4:
        sys.exit('Usege: python uaclient.py config method option')
