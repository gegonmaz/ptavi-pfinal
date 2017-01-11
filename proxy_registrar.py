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

class ProxyRegistraHandler(ContentHandler):

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
        self.DataBase = 'BaseDeDatos.txt'
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

    def baseDeDatos( self, archivo)
        archivoDatos = open(self.DataBase, 'r')
        linea = archivo.readLines()
        for l en linea:
            if linea.split(':')[0] == archivo.split(':')[0]:
                encontrado = True
            if not encontrado:
                archivoDatos.write(archivo + '\r\n')
        archivo.Datos.close()

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    Metodos = ['INVITE', 'BYE', 'ACK']

    def handle(self):
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print("El cliente nos manda " + line.decode('utf-8'))
            # Partimos el mensaje
            # Tendremos que guardar la traza
            Mensaje_Cliente = line.decode('utf-8').split()
            # Analizamos la linea para ver que metodo nos llega y contestar
            # Comprobamos el tamaño del paquete recibido
            if not line:
                break
            if Mensaje_Cliente[0] == 'INVITE':
                # INVITE --> tendremos que establecer la llamada(Comunicacion)
                envio = ("SIP/2.0 100 Trying\r\n\r\nSIP/2.0 180 Ring\r\n\r\n" +
                         "SIP/2.0 200 OK\r\n\r\n")
                envio += 'Content-Type: application/sdp\r\n\r\n'
                sdp = ('v=0\r\n' + 'o=' + \
                        self.listaEtiquetas['account']['username'] + \
                        ' ' + self.listaEtiquetas['uaserver']['ip'] + \
                        's=misesion\r\n' + \
                        't=0\r\n' + 'm=audio ' + \ 
                        self.listaEtiquetas['rtpaudio']['puerto'] + \
                        ' RTP\r\n\r\n')               
                envio += envio + sdp
                self.wfile.write(bytes(envio, 'utf-8'))
            elif Mensaje_Cliente[0] == 'ACK':
                os.system("./mp32rtp -i " + I127.0.0.1 + " -p " + \
                            self.listaEtiquetas['rtpaudio']['puerto'] + \
                            "<" + audio)
            elif Mensaje_Cliente[0] == 'BYE':
                # BYE --> se cierra la comunicación
                envio = self.wfile.write(b'SIP/2.0 200 Ok\r\n\r\n')
            if not Mensaje_Cliente[0] in self.Metodos:
                # if not Mensaje_Cliente[0] == 'INVITE'|'BYE'|'ACK':
                envio = self.wfile.write((b'SIP/2.0 405 Method Not Allowed') +
                                         (b'\r\n\r\n'))
            else:
                envio = self.wfile.write(b'SIP/2.0 400 Bad Request\r\n\r\n')

if __name__ == "__main__":

    parser = make_parser()
    cHandler = UASeverHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(FicheroXML)
    # Aqui tendremos que tener en cuenta la existencia de dos parametros
    try:
        IpUsuario = handler.listaEtiquetas['uaserver']['ip']
        Puerto = handler.listaEtiquetas['uaserver'][['puerto']
        serv = socketserver.UDPServer((IpUsuario, puerto), EchoHandler)
    except:
        sys.exit('Usage: python server.py Ip&Port cancion.mp3')

    handler.archivoLog('Empezamos...')
    # Tendremos que crear el socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        my_socket.connect((listaEtiquetas['regproxy']['ip'],
        int(listaEtiquetas['regproxy']['puerto']))

        handler.registrar()
        try:
            # Mientras este activo funcionara
            serv.serve_forever()
        except:
            # Cuando se interrumpa, se enviara la traza al fichero log
            handler.archivoLog('Terminamos... ')
