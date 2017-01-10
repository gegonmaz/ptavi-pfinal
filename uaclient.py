#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un cliente-servidor
"""

""" 
Agente del cliente
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

    """
    Tendremos que crear un archivo log; de modo que si cae el servicio,
    se pueda saber que usuarios estaban contectados en cada momento
    """
    def InicializacionElementos(self,name,attrs):
        #Buscaremos las etiquetas en el diccionario
        if name in self.diccionarioConfig:
            Valores = {}
            for etiquetas in self.diccionarioConfig[name]:
                Valores[name] = attrs.get(etiquetas, '')
            listaNombres = {name: Valores}
            self.listaEtiquetas.append(listaNombres)

    """
    Una vez inicializadas, tendremos que crear alguna funcion que nos permita
    acceder a las etiquetas
    """



if __name__ == "__main__":

