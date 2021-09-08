# -*- coding: utf-8 -*-

# Implementación de un parser: reconoce expresiones compuestas de lexemas
# a través de la implementación de la gramática con Descenso Recursivo
#
# Autores:
# José Elías Garza Vázquez    A00824494
# Einar López Altamirano      A01656259
# Francisco Garza González    A01193705
# Septiembre 2021

# Grámatica:
# <prog> ::= <exp> <prog> | $
# <exp> ::= <átomo> | <lista>
# <átomo> ::= símbolo | <constante>
# <constante> ::= número | booleano | string
# <lista> ::= ( <elementos> )
# <elementos> ::= <exp> <elementos> | epsilon

import sys
import return_token as scanner

# empata y obtiene el token siguiente
def match(expectedToken):
    global token
    if token == expectedToken:
        token = scanner.get_token()
    else:
        error("Wrong token")

# Función principal: flujo principal del análisis sintáctico
def parser():
    global token
    html = open('index.html', 'w') # abre archivo html en modo escritura (sobreescribe)
    # inserta los primeros elementos del DOM 
    html.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n<link href="style.css" rel="stylesheet" type="text/css">\n</head>\n<body>\n')
    html.close()
    token = scanner.get_token()
    prog()
    # abre el archivo en append mode para finalizarlo
    html = open('index.html', 'a')
    html.write('</body>\n</html>') 
    html.close()

# Programa
def prog():
    if token == scanner.SYM or token == scanner.NUM or token == scanner.STR or token == scanner.BOO or token == scanner.LRP:
        exp()
        prog()
    else:
        if token == scanner.END:
            print("Expresion bien construida")
        else:
            error("Expresion mal terminada")

# Expresión
def exp():
    if token == scanner.LRP:
        print("Inside exp", token)
        lis()
    else:
        atm()

# Átomo
def atm():
    if token == scanner.SYM:
        match(token)
    else:
        con()

# Constante
def con():
    if token == scanner.NUM:
        match(token)
    elif token == scanner.BOO:
        match(token)
    elif token == scanner.STR:
        match(token)
    else:
        error("Se esperaba una constante")

# Lista
def lis():
    match(scanner.LRP)  # reconoce Delimitador (
    ele()
    match(scanner.RRP)

# (Elemento)
def ele():
    if token == scanner.SYM or token == scanner.NUM or token == scanner.STR or token == scanner.BOO or token == scanner.LRP:
        exp()
        ele()

# Error sintáctico
def error(msg):
    print('ERROR:', msg)
    # se sustituye html actual con html de error
    html = open('index.html', 'wb') # borra y abre en modo escritura binaria (para grabar caracteres acentuados)
    err_msg = '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n<link href="style.css" rel="stylesheet" type="text/css">\n</head>\n<body>\n<err>>> ERROR SINTÁCTICO <<</err>\n</body>\n</html>'
    html.write(err_msg.encode('utf8')) # encoding
    html.close()
    sys.exit(1)
