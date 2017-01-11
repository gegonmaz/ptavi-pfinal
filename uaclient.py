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
    """
    # Variables que necesitaremos en los siguientes metodos
    IpProxy = handler.listaEtiquetas[3]['regproxy']['ip']
    PuertoProxy = handler.listaEtiquetas[3]['regproxy']['puerto']
    ArchivoLog = handler.listaEtiquetas[4]['log']['path']
    Usuario = handler.listaEtiquetas[0]['account']['username']
    ContraseñaUsuario = handler.listaEtiquetas[0]['account']['password']
    """

    """
    Como vamos a tener que estar constantemente enviando los mensajes, 
    crearemos un metodo para solo tener que llamar al metodo.
    """
    def envioMensajes(self, mensaje)
        my_socket.send(bytes(mensaje, 'utf-8'))

    """
    El cliente se tiene que registrar, tendrá que hacer la invitación de la
    llamada, realizar los ack al proxy y desconectarse, por tanto los podriamos
    implementar como metodos.
    """
    def registrar(self, TiempoExpiracion):

        if Metodo == 'REGITER':
            c = 'Expires: ' + str(TiempoExpiracion) + '\r\n\r\n'
            cabeceraRegistro = Metodo + 'sip: ' + 
                               self.listaEtiquetas['uaserver']['puerto'] + \ 
                               ' SIP/2.0\r\n'
            lineaEnvio = cabeceraRegistro + c
            self.envioMensaje(lineaEnvio)
            print(lineaEnvio)
            # Pero tendrá que esperar respuesta
            mensajeServidor = my_socket.recv(1024).decode('utf-8')
            print('El servidor manda: ' + mensajeServidor)
            """
            Ahora es cuando se registrara el usuario, por tanto tendra que 
            facilitar una contraseña. Que a su vez tambien tendremos que 
            guardar en el archivo log. Se tendra que utilizar una funcion hash
            """
            if mensajeServidor == 'SIP/2.0 401 Unauthorized'
                """
                Al ser autorizado, en la cabecera se tendrá que enviar el 
                tiempo de expiracion mas una cabecera con utenticacion
                """
                
    def invitar(self, Usuario)
        """
        La cabecera acabara con Content-Type: application/sdp y el sdp
        """
        if Metodo == 'INVITE':
            tipo = 'Content-Type: application/sdp\r\n\r\n'
            sdp = 'v=0\r\n' + 'o=' + diccionarioConfig['account']['username']+\ 
            ' ' + diccionarioConfig['uaserver']['ip'] + 's=misesion\r\n' + \
            't=0\r\n'  + 'm=audio ' + diccionarioConfig['rtpaudio']['puerto']+\
            ' RTP\r\n'
            lineaEnvio = Metodo + ' sip:' + Usuario + ' SIP/2.0\r\n' + tipo + \
            sdp
            self.envioMensaje(lineaEnvio)
            print('Mensaje enviado: ' + lineaEnvio)

            # y tendrá que esperar una respuesta del servidor
            datos = my_socket.recv(1024)
            

    def asentimiento(self, Usuario)
        if Metodo == 'ACK':
            lineaEnvio = 'ACK sip:' + Usuario + ' SIP72.0'
            self.envioMensaje(lineaEnvio)
            print('Asentimiento: ' + lineaEnvio)

    def desconexion(self, Usuario)
        if Metodo == 'BYE':
            lineaEnvio = 'BYE

if __name__ == "__main__":

    # Tendremos que crear el socket 
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    # Esta vez en vez de anudarlo a un servidor, lo haremos al Proxy
    my_socket.connect((diccionarioConfig['regproxy']['ip'], 
                       int(diccionarioConfig['regproxy']['puerto']))

    # El programa tendrá que actuar segun el metodo que haya recibido
    
    if len(sys.argv) != 4:
        sys.exit('Usege: python uaclient.py config method option')
