#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import socketserver
import sys
import csv
import urllib.request
import hushlib
import time
from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class UAServerHandler(ContentHandler):

    """
    User Agent del cliente
    """
    """
    Vamos a crear una funcion que se encargue de crear un diccionario con
    las etiquetas del archivo XML para ir guardando los datos.
    """
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
    # Creamos las variables global para poder utilizarlas durante el prog.

    def __init__(self):

        self.listaEtiquetas = []
        self.diccionarioConfig = {'server': ['name', 'ip', 'puerto'],
                                  'database': ['path', 'passwdpath'],
                                  'log': ['path']}
    """
    Vamos a tener que inicializar todos los elementos(etiquetas) del
    diccionario creado anteriormente
    """
    def InicializacionElementos(self, name, attrs):
        # Buscaremos las etiquetas en el diccionario
        if name in self.diccionarioConfig:
            Valores = {}
            for etiquetas in self.diccionarioConfig[name]:
                Valores[name] = attrs.get(etiquetas, '')
            listaNombres = {name: Valores}
            self.listaEtiquetas.append(listaNombres)

    # Variables que necesitaremos en los siguientes metodos
    IpProxy = handler.listaEtiquetas[3]['regproxy']['ip']
    PuertoProxy = handler.listaEtiquetas[3]['regproxy']['puerto']
    ArchivoLog = handler.listaEtiquetas[4]['log']['path']
    Usuario = handler.listaEtiquetas[0]['account']['username']
    ContraseñaUsuario = handler.listaEtiquetas[0]['account']['password']
    PuertoServidor = handler.listaEtiquetas[1]['uaserver']['puerto']

    """
    Una vez inicializadas, tendremos que crear alguna funcion que nos permita
    acceder a las etiquetas
    """
    def get_tags(self):
        # Nos tendrá que devolver la lista segun como este
        return self.listaEtiquetas

    """
    Tendremos que crear un archivo log; de modo que si cae el servicio,
    se pueda saber que usuarios estaban contectados en cada momento
    """
    def archivoLog(self, mensaje):
        # Primero aseguramos si existe algún fichero ya
        fichero = open(self.listaEtiquetas['log']['path'], 'a')
        tiempo = time.strtime('%Y%m%H%M%S', time.gmtime(time.time()))
        linea = str(tiempo) + ' ' + mensaje + '\r\n'
        fichero.write(linea)
        fichero.close()
        print(linea[:-1])

    def envioMensajes(self, mensaje):
        my_socket.send(bytes(mensaje, 'utf-8'))
