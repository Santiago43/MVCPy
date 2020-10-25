#!/usr/bin/python3

import cgi
from MVCPy.models.usuario import Usuario
from MVCPy.dao.usuariosDao import UsuariosDao
print('Content-Type: text/html')
print('')

datos= cgi.FieldStorage()
nombre=datos.getvalue('nombre')
contra =datos.getvalue('contra')
usuario=Usuario(nombre,contra)
dao=UsuariosDao()
consulta = dao.consultar(nombre,contra)
