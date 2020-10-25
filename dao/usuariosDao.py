#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from dao import dao
from MVCPy.models.usuario import Usuario
class UsuariosDao(dao):
    """
    docstring
    """
    def registrar(self,usuario):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "insert into registrado (username,pass) values (%s,sha(%s));"
            cursor.execute(sql,(usuario.nombre,usuario.contraseña))
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return False
    def consultar(self,username,password):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select username, pass from registrado where username='"+str(username)+"'and pass=sha('"+str(password)+"');"
            cursor.execute(sql)
            usuario = Usuario()
            for row in cursor:
                usuario.nombre=row[0]
                usuario.contraseña=row[1]
            cursor.close()
            cnx.close()
            return usuario
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return None



