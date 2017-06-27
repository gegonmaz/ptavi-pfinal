#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import socketserver
import sys
import csv
import urllib.request
import hashlib
import time
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
"""
Clase (y programa principal) para un cliente-servidor
"""


class UAClientHandler(ContentHandler):

    """
    User Agent del cliente
    """
    """
    Vamos a crear una funcion que se encargue de crear un diccionario con
    las etiquetas del archivo XML para ir guardando los datos.
    """
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
    def InicializacionElementos(self, name, attrs):
        # Buscaremos las etiquetas en el diccionario
        if name in self.diccionarioConfig:
            Valores = {}
            for etiquetas in self.diccionarioConfig[name]:
                Valores[name] = attrs.get(etiquetas, '')
            listaNombres = {name: Valores}
            self.listaEtiquetas.append(listaNombres)

    """
    # Variables que necesitaremos en los siguientes metodos
    IpProxy = handler.listaEtiquetas[3]['regproxy']['ip']
    PuertoProxy = handler.listaEtiquetas[3]['regproxy']['puerto']
    ArchivoLog = handler.listaEtiquetas[4]['log']['path']
    Usuario = handler.listaEtiquetas[0]['account']['username']
    ContraseñaUsuario = handler.listaEtiquetas[0]['account']['password']
    PuertoServidor = handler.listaEtiquetas[1]['uaserver']['puerto']
    """

    """
    Una vez inicializadas, tendremos que crear alguna funcion que nos permita
    acceder a las etiquetas
    """
    def obtenerEtiquetas(self):
        # Nos tendrá que devolver la lista segun como este
        """Devuelve los datos, con formato, obtenidos de "ua1.xml"."""
        doc = ""
        for dict_listaEtiquetas in self.listaEtiquetas:
            for key in dict_listaEtiquetas:
                doc = doc + key + "\t"
                for k_2 in dict_listaEtiquetas[key]:
                    doc = doc + k_2 + '="' + dict_listaEtiquetas[key][k_2] + '"' + "\t"
                doc = doc + "\n"

        return doc
    def recibirMensaje(self):
        u"""Método para mediante el cual recibiremos los mensajes Recibir."""
        try:
            data = my_socket.recv(1024)
        except:
            log_txt = "Error: servidor no alcanzado " + proxy_ip
            log_txt += " puerto " + proxy_port + "\r\n"
            handler.to_log_txt(log_txt)
            sys.exit()

        #Guardamos en el LOG.
        proxy_ip = handler.listaEtiquetas[3]["regproxy"]["ip"]
        proxy_port = handler.listaEtiquetas[3]["regproxy"]["puerto"]
        data_rcv = data.decode("utf-8")
        log_ip_port = "recibirMensaje de " + proxy_ip + ":" + proxy_port + ": "
        data_log = log_ip_port + data_rcv
        self.to_log_txt(data_log)

        #Respuesta No Autorizado.
        if data_rcv[:11] == "SIP/2.0 401":
            nonce = data_rcv[data_rcv.find('"')+1:data_rcv.rfind('"')]
            m = hashlib.sha1()
            PASSWORD = self.listaEtiquetas[0]["account"]["passwd"]

            m.update(bytes(PASSWORD + nonce, 'utf-8'))
            Dig_resp = m.hexdigest()

            acc_username = self.listaEtiquetas[0]["account"]["username"]
            serv_port = self.listaEtiquetas[1]["uaserver"]["puerto"]

            #Nuevo Mensaje con info de registro.
            head_register = "REGISTER sip:" + acc_username + ":" + serv_port
            head_register += " SIP/2.0\r\nExpires: " + OPTION
            head_register += '\r\nAuthorization: Digest response="'
            head_register += Dig_resp + '"' + "\r\n\r\n"
            self.send(head_register)

            #Guardamos en el LOG.
            log_msg = "Sent to " + self.listaEtiquetas[3]["regproxy"]["ip"] + ":"
            log_msg += self.listaEtiquetas[3]["regproxy"]["puerto"]
            log_msg += ": " + head_register
            self.to_log_txt(log_msg)

            #Recibiremos OK.
            self.recibirMensaje()

        #Recibimos TRYING/RINGING/OK.
        elif data_rcv[:11] == "SIP/2.0 100":
            self.Ack(OPTION)


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
        print(linea)

    def envioMensajes(self, mensaje):
        my_socket.send(bytes(mensaje, 'utf-8'))

    def registrar(self, TiempoExpiracion):

        if Metodo == 'REGITER':
            c = 'Expires: ' + str(TiempoExpiracion) + '\r\n\r\n'
            cabeceraRegistro = self.Metodo + 'sip: ' + \
            self.listaEtiquetas['uaserver']['puerto'] + ' SIP/2.0\r\n'
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
            MensajeEnviado = 'Mensaje enviado por: ' + IpProxy + IpPuerto
            MensajeLog = MensajeEnviado + mensajeServidor
            self.archivoLog(MensajeLog)
            if mensajeServidor == 'SIP/2.0 401 Unauthorized'
                nonce = mensajeServidor.split('"')[1]
                # Ahora tendremos que utilizar la funcion hash
                respuesta = hashlib.sha1()
                respuesta.update(bytes(listaEtiquetas['account']['password'], \
                                       'utf-8'))
                respueta.update(bytes(nonce, 'utf-8'))
                respuesta = respuesta.hexdigest()

                # Ahora se tendra que  dar la respuesta con la autorizacion
                CabeceraNueva = 'REGISTER sip:' + self.Usuario + \
                                self.PuertoServidor
                CabeceraNueva += ' SIP/2.0\r\n' + 'Expires: ' + \
                                 TiempoExpiracion + '\r\n'
                CabeceraNueva += 'Authorization: Digest response=' + \
                                 self.respuesta + '\r\n'
                self.envioMensaje(CabeceraNueva)
                # Ahora habra uqe guardar un registro en el archivo log.
                MensajeEnviado = 'Mensaje enviado por: ' + IpProxy + IpPuerto
                MensajeLog = MensajeEnviado + mensajeServidor + ':' + \
                CabeceraNueva + '\r\n'
                self.archivoLog(MensajeLog)
                # Ahora el servidor nos habra aceptado y recibiremos el 200 OK
                mensajeServidor = my_socket.recv(1024).decode('utf-8')
                print('El servidor manda: ' + mensajeServidor)

    def invitar(self, Usuario):
        """
        La cabecera acabara con Content-Type: application/sdp y el sdp
        """
        if Metodo == 'INVITE':
            tipo = 'Content-Type: application/sdp\r\n\r\n'
            sdp = 'v=0\r\n' + 'o=' + listaEtiquetas['account']['username'] + \
                    ' ' + diccionarioConfig['uaserver']['ip'] + \
                    's=misesion\r\n' + \
                    't=0\r\n' + 'm=audio ' + \
                    listaEtiquetas['rtpaudio']['puerto'] + ' RTP\r\n'
            lineaEnvio = Metodo + ' sip:' + Usuario + ' SIP/2.0\r\n' + tipo + \
                            sdp
            self.envioMensaje(lineaEnvio)
            print('Mensaje enviado: ' + lineaEnvio)

            # Tendra que guardar las trazas de la invitacion a la conversacion
            MensajeEnviado = 'Mensaje enviado por: ' + IpProxy + IpPuerto
            MensajeLog = MensajeEnviado + lineaEnvio + ':' + '\r\n'
            self.archivoLog(MensajeLog)

            # y tendrá que esperar una respuesta del servidor
            mensajeServidor = my_socket.recv(1024).decode('utf-8')
            print('El servidor manda: ' + mensajeServidor)

    def asentimiento(self, Usuario):
        if Metodo == 'ACK':
            lineaEnvio = 'ACK sip:' + Usuario + ' SIP72.0'
            self.envioMensaje(lineaEnvio)
            print('Asentimiento: ' + lineaEnvio)

            # Guardamos trazas
            MensajeEnviado = 'Mensaje enviado por: ' + IpProxy + IpPuerto
            MensajeLog = MensajeEnviado + lineaEnvio + ':' + '\r\n'
            self.archivoLog(MensajeLog)

    def desconexion(self, Usuario):
        if Metodo == 'BYE':
            lineaEnvio = 'BYE sip:' + Usuario + 'SIP/2.0'
            self.envioMensaje(lineaEnvio)
            print('Se desconecto: ' lineaEnvio)

            # Guardamos trazas
            MensajeEnviado = 'Mensaje enviado por: ' + IpProxy + IpPuerto
            MensajeLog = MensajeEnviado + lineaEnvio + ':' + '\r\n'
            self.archivoLog(MensajeLog)

            datos = my_socket.recv(1024)

if __name__ == "__main__":

    # Tendremos que crear el socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        my_socket.connect((listaEtiquetas['regproxy']['ip'],
        int(listaEtiquetas['regproxy']['puerto']))
        if len(sys.argv) != 4:
            sys.exit('Usege: python uaclient.py config method option')
        parser = make_parser()
        cHandler = UAClientHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(FicheroXML)
        # Crear trazas de inicio en el archivo log para saber cuando empieza prog.
        handler.archivoLog('Inicio... ')

        Metodos = ['INVITE', 'BYE', 'ACK']

        if Metedo == 'REGISTER'
            hanler.registrar(TiempoExpiracion)
        elif Metodo == 'INVITE'
            handler.invita(Usuario)
        else Metodo == 'BYE'
            handler.desconexion(Ususario)
            my_socket.close()
            print('Fin de conexion')
        handler.archivoLog('Terminamos...' + ' ')
