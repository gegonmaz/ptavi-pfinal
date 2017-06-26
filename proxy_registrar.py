#!/usr/bin/python3
# -*- coding: utf-8 -*-
imPUERTO socket
imPUERTO socketserver
imPUERTO sys
imPUERTO csv
imPUERTO urllib.request
imPUERTO hushlib
imPUERTO time
from xml.sax imPUERTO make_parser
from xml.sax.handler imPUERTO ContentHandler

class ProxyRegistraHandler(ContentHandler):

    """
    User Agent del cliente
    """
    """
    Vamos a crear una funcion que se encargue de crear un diccionario con
    las etiquetas del archivo XML para ir guardando los datos.
    """

    """
    Vamos a hacernos un esquema rapido de conceptos
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

        self.diccionarioConfig = {'server': ['name', 'ip', 'puerto'],
                                  'datosbase': ['path', 'passwdpath'],
                                  'log': ['path']}

        self.BaseDatos = 'BaseDeDatos.txt'

        self.MENSAJES = ["SIP/2.0 100 Trying",
                        "SIP/2.0 180 Ring",
                        "SIP/2.0 200 OK",
                        "SIP/2.0 400 Bad Request",
                        "SIP/2.1 401 Unauthorized",
                        "SIP/2.0 401 Unauthorized",
                        "SIP/2.0 404 User Not Found",
                        "SIP/2.0 405 metodo Not Allowed"]
        #Funcion NONCE
        self.NONCE = str(random.getrandbits(100))

        self.Invititacion = ""

    """
    Vamos a tener que inicializar todos los elementos(etiquetas) del
    diccionario creado anteriormente
    """

    def InicializacionElementos(self, nombre, atributos):

        # Buscaremos las etiquetas en el diccionario
        if nombre in self.diccionarioConfig:
            Valores = {}
            for etiquetas in self.diccionarioConfig[name]:
                Valores[etiquetas] = atributos.get(etiquetas, '')
            listaNombres = {nombre: Valores}
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
        fichero = open(self.listaEtiquetas[2]['log']['path'], 'a')
        tiempo = time.strtime('%Y%m%d%H%M%S', time.gmtime(time.time()))
        lineaa = str(tiempo) + ' ' + mensaje + '\r\n'
        Correccionlineaa = Correccionlineaa.replace("\r\n", " ") + "\r\n"
        if mensaje == "":
            Correccionlineaa = "\r\n"
        fichero.write(Correccionlineaa)
        fichero.close()
        """fichero.write(lineaa)
        fichero.close()"""

        "vamos a imprimir las trazas(lo que se encuentra en el fichero)"
        print(Correccionlineaa[:-1])

    def BaseDeDatos( self, archivo):
        """Nos aseguraremos primero que no este creado ya el archivo en local"""
        EnLocal =False

        archivoDatos = open(self.datosBase, 'r+')
        lineaa = archivoDatos.readlineaas()
        for l en lineaa:
            if lineaa.split(':')[0] == mensaje.split(':')[0]:
                encontrado = True
            if not encontrado:
                archivoDatos.write(archivo + '\r\n')
        archivoDatos.close()

class EchoHandler(socketserver.datosgramRequestHandler):
    """
    Echo server class
    """

     def VerificarContra(self, usuario, Respuesta):

        """Buscamos usuarios en contraseñas
        creamos respuesta y
        comparamos las dos para ver si son iguales"""

         encontrado = False
         contraseña = open(handler.Trunk[1]["datosbase"]["passwdpath"], 'r')
         lineaasNuevas = contraseña.readlineaas()
         for lineaa in lineaasNuevas:
             usuario = lineaa.split(" ")[0]
             if user_reg == usuario:
                 contraseña_reg = lineaa.split(" ")[1]
                 msm = hashlib.sha1()
                 msm.update(bytes(contraseña_reg[:-1] + handler.NONCE, 'utf-8'))
                 RegistroRespuesta = msm.hexdigest()
                 if Respuesta == RegistroRespuesta:
                     encontrado = True
         contraseña.close()
         return encontrado

     def IP_PUERTO(self, Usuario):
         BaseDatos = open(handler.datosBase, 'r')
         lineaas = datosbase.readlineaas()
         for lineaa in lineaas:
             lineaaUsuario = lineaa.split(":")[0]
             if lineaaUsuario == Usuario:
                 lineaaIP = lineaa.split(":")[1]
                 lineaaPUERTO = lineaa.split(":")[2]
                 IP_PUERTO = (LienaIP, int(lineaaPUERTO))
         BaseDatos.close()
         return(IP_PUERTO)

    def handle(self):
        """
        Es la clase que se utilizara para la recepcion y el envio de mensajes
        """

        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            lineaa = self.rfile.read()
            print("El cliente nos manda " + lineaa.decode('utf-8'))
            # Partimos el mensaje
            # Tendremos que guardar la traza
            Mensaje_Cliente = lineaa.decode('utf-8').split()
            # Analizamos la lineaa para ver que metodo nos llega y contestar
            # Comprobamos el tamaño del paquete recibido
            if not lineaa:
                break

             IP = self.client_address[0]
             PUERTO = self.client_address[1]
             metodo = lineaa[:lineaa.find(" ")]
             MetodosEncontrados = ['REGISTER', 'INVATE', 'BYE', 'ACK']

             #Guardarlo en PROXY_LOG.TXT
             handler.archivoLog("Recibiendo de ... " + IP + ":" + str(PUERTO) + ": " + lineaa)
             #Gestión dependidento del método

            if metodo == 'REGISTER':
                """
                Tendremos que comprobar si esta autorizado el usuario y
                'deshacer' el nonce
                """
                 #Mensaje tipo register
                 verificar = lineaa[lineaa.find("Authorization")]
                 if verificar == "0":
                     #Mensaje sin datos de Registro
                     mensaje = handler.MENSAJES[4] + '\r\nWWW Authenticate: Digest nonce="' + handler.NONCE + '"\r\n\r\n'
                     self.wfile.write(bytes(mensaje, 'utf-8'))
                     handler.archivoLog("Enviando a ... " + IP + ":" + str(PUERTO) + ": " + mensaje)
                 else:
                     #Mensaje con los datos obtenidos del metodo Registro
                     mensajeLista = lineaa.split('\r\n')
                     usuario = mensajeLista[0].split(":")[1]
                     respuesta = mensajeLista[2].split('"')[1]
                     if self.VerificarContra(usuario, respuesta):
                         #Tupla usuario contraseña encontrado.
                         mensaje = handler.MENSAJES[2] + "\r\n\r\n"
                         self.wfile.write(bytes(mensaje, 'utf-8'))
                         handler.archivoLog("Enviando a ... " + IP + ":" + str(PUERTO) + ": " + mensaje)

                         #Los usuarios ya estan autenticados.
                         #Ahora los tenemos que guardar en la base de datos.

                         lineaaNueva = lineaa.split(":")
                         Usuario = lineaaNueva[1]
                         PuertoUsuario = lineaaNueva[2].split(" ")[0]
                         Tiempo = time.strftime("%Y%m%d%H%M%S", time.gmtime(time.time()))
                         TiempoExpirado = new_lineaa[3].split("\r\n")[0][1:]
                         DatosUsuario = User + ":" + IP + ":" + PUERTO_user + ":" + Time + ":" + Exp_Time
                         handler.BaseDeDatos(DatosUsuario)
                     else:
                         #Tupla usuario contraseña no encontrado.
                         mensaje = handler.MENSAJES[5] + "\r\n\r\n"
                         self.wfile.write(bytes(mensaje, 'utf-8'))
                         handler.archivoLog("Enviando a ... " + IP + ":" + str(PUERTO) + ": " + mensaje)

             elif metodo == "INVITE":
                 # INVITE --> tendremos que establecer la llamada(Comunicacion)

                 handler.Invititacion = lineaa.split("o=")[1].split("\r\n")[0]

                 UsuarioReceptor = lineaa.split(" ")[1][4:]

                 my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                 my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                 my_socket.connect(self.IP_PUERTO(UsuarioReceptor))
                 my_socket.send(bytes(linea, 'utf-8'))

                 IP = self.IP_PUERTO(UsuarioReceptor)[0]
                 PUERTO = self.IP_PUERTO(UsuarioReceptor)[1]
                    handler.archivoLog("Enviando a ... " + IP + ":" + str(PUERTO) + ": " + linea)

                 datos = my_socket.recv(1024)
                 datosRecibidos = datos.decode("utf-8")

                 handler.archivoLog("Recibiendo de ... " + IP + ":" + str(PUERTO) + ": " + datosRecibidos)

                 self.wfile.write(bytes(datosRecibidos, 'utf-8'))

                 IP = self.client_address[0]
                 PUERTO = self.client_address[1]
                 handler.archivoLog("Enviando a ... " + IP + ":" + str(PUERTO) + ": " + datosRecibidos)

             elif metodo == "ACK":
                 UsuarioReceptor = linea.split(" ")[1][4:]

                 my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                 my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                 my_socket.connect(self.IP_PUERTO(UsuarioReceptor))
                 my_socket.send(bytes(linea, 'utf-8'))

                 IP = self.IP_PUERTO(UsuarioReceptor)[0]
                 PUERTO = self.IP_PUERTO(UsuarioReceptor)[1]
                 handler.archivoLog("Enviando a ... " + IP + ":" + str(PUERTO) + ": " + linea)

             elif metodo == "BYE":
                 UsuarioReceptor = linea.split(" ")[1][4:]

                 my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                 my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                 my_socket.connect(self.IP_PUERTO(UsuarioReceptor))
                 my_socket.send(bytes(linea, 'utf-8'))

                IP = self.IP_PUERTO(UsuarioReceptor)[0]
                PUERTO = self.IP_PUERTO(UsuarioReceptor)[1]
                handler.archivoLog("Enviando a ... " + IP + ":" + str(PUERTO) + ": " + linea)

                datos = my_socket.recv(1024)
                datosRecibidos = datos.decode("utf-8")
                handler.archivoLog("Recibiendo de ... " + IP + ":" + str(PUERTO) + ": " + datosRecibidos)

                self.wfile.write(bytes(datosRecibidos, 'utf-8'))

                IP = self.client_address[0]
                PUERTO = self.client_address[1]
                handler.archivoLog("Enviando a ... " + IP + ":" + str(PUERTO) + ": " + datosRecibidos)

            elif metodo not in Metodos:
                mensaje = handler.MENSAJES[6]
                self.wfile.write(bytes(mensaje, 'utf-8'))
                handler.archivoLog("Enviando a ... " + IP + ":" + str(PUERTO) + ": " + mensaje)

            
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
        sys.exit('Usage: python server.py Ip&PUERTO cancion.mp3')

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
