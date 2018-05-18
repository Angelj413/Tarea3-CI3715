#!/usr/bin/python3
"""
Titulo: seguridad.py

Descripcion: Implementacion de la clase Seguridad.

Autores: Angel Morante

Equipo: Null Pointer Exception

Fecha:11/05/2018.
"""

"""
La clase Seguridad representa una interfaz para la validacion de usuarios en
una aplicacion web.

Tiene un atributo users de tipo dict que almacena los datos de loggeo de los
usuarios que acceden a la aplicacion de forma que el usuario es la clave y el
dato es su clave. 

Los metodos son de inicializacion (init), verificar_email, verificar_psswd,
registrarUsuario e ingresarUsuario.
"""
import re

class Seguridad():
    #Constructor de la clase, se definen los atributos de la misma
    #Nota: se hace uso de la libreria de python re.py para operaciones con expreciones regulares
    def __init__(self):
        self.users = {}
        self.email_format = re.compile(
            '([a-zA-Z0-9]+)@([a-zA-Z0-9]+)(\.)([a-zA-Z0-9]+)')
        self.no_alfan = re.compile('.*[^a-zA-Z0-9]+.*')
        self.letras_3 = re.compile('.*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*')
        self.mayus_01 = re.compile('.*[A-Z].*')
        self.minus_01 = re.compile('.*[a-z].*')
        self.digit_01 = re.compile('.*[0-9].*')

    # Metodo que toma tres string, apuntados por email, pswd1 y pswd2
    # La funcionalidad del metodo consiste en verificar si el correo 
    # electronico tiene un formato valido, las claves coinciden y
    # cumplen con los requisitos formulados mas abajo:
    """ El formato del correo electronico debe cumplir con el Internet e-mail address format
        (RFC 822) y la clave debe satisfacer los siguientes requerimientos:
            1.1 Su longitud debe estar entre 8 y 16 caracteres
            1.2 No debe incluir caracteres especiales (solo letras mayusculas, letras minusculas y
        digitos)
    """
    def registrarUsuario(self, email, pswd1, pswd2):
        id_email = self.email_format.match(email) != None
        nw_email = email not in self.users
        minimo = len(pswd1) > 7
        maximo = len(pswd1) < 17
        pnoalfan = self.no_alfan.match(pswd1) == None
        p3letras = self.letras_3.match(pswd1) != None
        pmayus01 = self.mayus_01.match(pswd1) != None
        pminus01 = self.minus_01.match(pswd1) != None
        pdigit01 = self.digit_01.match(pswd1) != None
        password = minimo and maximo and pnoalfan and p3letras and pmayus01
        password = password and pminus01 and pdigit01
        samepass = pswd1 == pswd2
        try:
            assert(id_email)
            assert(nw_email)
            assert(password)
            assert(samepass)
            self.users[email] = pswd1
        except:
            if not id_email:
                print("Correo electronico invalido")
            if not nw_email:
                print("Correo electronico ya existe")
            if not password:
                print("Clave invalida")
            if not minimo:
                print("La clave tiene menos de 8 caracteres")
            if not maximo:
                print("La clave tiene mas de 16 caracteres")
            if not pnoalfan:
                print("La clave tiene algun caracter especial: !,*,...")
            if not p3letras:
                print("La clave tiene menos de 3 letras")
            if not pmayus01:
                print("La clave no tiene mayusculas")
            if not pminus01:
                print("La clave no tiene minusculas")
            if not pdigit01:
                print("La clave no tiene numeros")
            if not samepass:
                print("Las claves no coinciden")
        finally:
            return id_email and nw_email and password and samepass

    # Metodo que toma dos strings apuntados por email y pswd y devuelve True y 
    # muestra el mensaje "Usuario aceptado" si y solo si:
    #    1. email se encuentra en el atributo users.
    #    2. pswd es igual al dato asociado a la clave email del atributo users.
    # Caso contrario, se retorna False y le da mensajes al usuario
    # correspondientes al error ocurrido.
    def ingresarUsuario(self, email, pswd):
        valid_email = email in self.users
        if valid_email:
            valid_psswd = self.users[email] == pswd
        try:
            assert(valid_email and valid_psswd)
            print("Usuario aceptado")
        except:
            if not valid_email:
                print("Usuario invalido")
            if valid_email and not valid_psswd:
                print("Clave invalida")
        finally:
            return valid_email and valid_psswd