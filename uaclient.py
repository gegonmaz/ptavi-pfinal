#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un cliente-servidor
"""

import socketserver
import sys

# este comando nos servirá para capturar los datos de la shell
import csv
import urllib.request
import json
import time

def lista_etiquetas(misdatos):

    listado = ""
    for etiqueta in misdatos:
        listado = listado + etiqueta[0]
        atribs = etiqueta[1].items()
        for atrib, contenido in atribs:
            if contenido != "":
                listado = listado + "\t" + atrib + "=" + '"' + contenido + '"'
        listado = listado + "\n"
    return listado


def to_json(misdatos):
"""
    Podremos utilizar este metodo para los archivos log
"""
    with open('log.json', 'w') as outfile_json:
            json.dump(misdatos, outfile_json, sort_keys=True, indent=3, 
            separators=(' ', ': '))


def info_ua(misdatos):

    list_ua = []
    for etiqueta in misdatos:
        atribs = etiqueta[1].items()
        for atrib, contenido in atribs:
            
            

            if atrib == "username":
                Nombre_usuario = contenido
                list_ua = Nombre_usuario
            else atrib == "password"
                Contraseña_usuario = contenido
                # f = open (filename, "wb")
                # f.write(passwords.read())
                # Tendremos que asignar cada caontraseña al usuario que pertenece
            if atrib == "ip"
                Ip_servidor = contenido
            else atrib == "puerto"
                Puerto_servidor == contenido
            if atrib == "puerto"
                Puerto_proxy = contenido
            if atrib == "ip"
                Ip_regproxy = contenido
            else atrib == "puerto"
                Puerto_regproxy = contenido
            if atrib == "path"
                localizacion_log == contenido
            if atrib == "path"
                localizacion_cancion = contenido
"""
------------------------------------------------------------------------------
"""



                if remoto == "http:":
                    arch_web = urllib.request.urlopen(url)
                    filename = list_url[-1]
                    print("Descargado..." + filename)
                    f = open(filename, "wb")
                    f.write(arch_web.read())
                else:
                    filename = contenido
                print("Este contenido ya está en local... " + filename)
