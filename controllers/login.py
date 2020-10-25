#!/usr/bin/python3
import cgi
from MVCPy.models.usuario import Usuario
from MVCPy.dao.usuariosDao import UsuariosDao
print('Content-Type: text/html')
print('')

datos= cgi.FieldStorage()
print(datos)
user=datos.getvalue('nombre')
password =datos.getvalue('contra')
dao=UsuariosDao()
usuario=dao.consultar(user,password)
if usuario is None:
    print("<p>Usuario o contrasena incorrectos</p>")
else:
    print("<p>Bienvenido {}</p>".format(usuario.nombre))