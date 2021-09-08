# -*- coding: utf-8 -*-

# Implementación de un scanner a través de la 
# representación de un AFD como Matriz de Transiciones 
# 
# Autores:
# José Elías Garza Vázquez    A00824494
# Einar López Altamirano      A01656259
# Francisco Garza González    A01193705
# Septiembre 2021

import sys

SYM = 100  # SYMBOL
NUM = 200  # NUMBER
BOO = 300  # BOOLEAN
STR = 400  # STRING
LRP = 501  # LEFT PARENTHESIS
RRP = 502  # RIGHT PARENTHESIS
END = 600  # END
ERR = 700  # ERROR

#      a-z 0-9   #   " t/f spc  \n   (   ) rar   $
MT = [[  1,  2,  3,  5,  1,  0,  0,LRP,RRP,  7,END],  # 0 -> Intial State
      [  1,  7,  7,  7,  1,SYM,SYM,SYM,SYM,  7,  7],  # 1 -> Symbol
      [  7,  2,  7,  7,  7,NUM,NUM,NUM,NUM,  7,  7],  # 2 -> Number
      [  7,  7,  7,  7,  4,ERR,  7,  7,  7,  7,  7],  # 3 -> # of Bool
      [  7,  7,  7,  7,  7,BOO,BOO,BOO,BOO,  7,  7],  # 4 -> t/f of Bool
      [  5,  5,  7,  6,  5,  5,  7,  7,  7,  7,  7],  # 5 -> String Char
      [  7,  7,  7,  7,  7,STR,STR,STR,STR,  7,  7],  # 6 -> Closing quotes Strings
      [  7,  7,  7,  7,  7,ERR,  7,  7,  7,  7,ERR]]  # 7 -> Error state

# Filtro de caracteres: retorna un número entero indicando la columa de la MT
# de acuerdo al caracter leido
def filter(c, file):
    '''Retorna un número entero indicando la columa de la MT de acuerdo al caracter leido'''
    if c == 't' or c == 'f':  # true of false
        return 4
    elif c == '0' or c == '1' or c == '2' or \
         c == '3' or c == '4' or c == '5' or \
         c == '6' or c == '7' or c == '8' or c == '9':  # 0-9
        return 1
    elif c == '#':  # hashtag
        return 2
    elif c == '"':  # Quote
        return 3
    elif ord(c) >= ord('a') and ord(c) <= ord('z'):  # a-z
        return 0
    elif c == ' ':  # blank space
        file.write('&nbsp;')
        return 5
    elif c == '\n':  # new line
        file.write('<br>')
        return 6
    elif c == '(':  # delimitator (
        return 7
    elif c == ')':  # delimiator )
        return 8
    elif c == '$':  # End
        return 10
    else:         # Rare char
        return 9

# Valores para realizar la lectura
_c = None
_read = True

# Función principal: retorna los tokens encontrados, realizando el analisis léxico
def get_token():
    '''Implementa un analizador léxico leyendo los caracteres de stdin'''
    html = open('index.html', 'a') # se abre archivo html en append mode
    global _c, _read
    state = 0
    lexeme = ""

    while(True):
        while state < 100:
            if _read:
                _c = sys.stdin.read(1)
            else:
                _read = True # indica si se puede leer otro caracter de stdin
            state = MT[state][filter(_c, html)]
            if state < 100 and state != 0: # mientras el estado no sea ACEPTOR ni ERROR
                lexeme += _c
        if state == SYM: # símbolo
            _read = False
            print("Symbol", lexeme)
            html.write('<sym>' + str(lexeme) + '</sym>') # se añade lexema a html con div SYM
            return SYM
        elif state == NUM: # número
            _read = False
            print("Number", lexeme)
            html.write('<num>' + str(lexeme) + '</num>') # se añade lexema a html con div NUM
            return NUM
        elif state == BOO: # booleano
            _read = False
            print("Boolean", lexeme)
            html.write('<boo>' + str(lexeme) + '</boo>') # se añade lexema a html con div BOO
            return BOO
        elif state == STR: # string
            _read = False
            print("String", lexeme)
            html.write('<str>' + str(lexeme) + '</str>') # se añade lexema a html con div STR
            return STR
        elif state == LRP: # (
            lexeme += _c
            print("Delimitator", lexeme)
            html.write('<lrp>' + str(lexeme) + '</lrp>') # se añade lexema a html con div LRP
            return LRP
        elif state == RRP: # )
            lexeme += _c
            print("Delimitator", lexeme)
            html.write('<rrp>' + str(lexeme) + '</rrp>') # se añade lexema a html con div RRP
            return RRP
        elif state == END: # $
            print("Fin de expresion")
            html.write('<end>' + '$' + '</end>') # se añade lexema a html con div END
            return END
        else: # error léxico
            _read = False
            print("Error, not accepted word", lexeme)
            # se sustituye html actual con html de error
            html.close()
            html = open('index.html', 'wb') # borra y abre en modo escritura binaria (para grabar caracteres acentuados)
            err_msg = '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n<link href="style.css" rel="stylesheet" type="text/css">\n</head>\n<body>\n<err>>> ERROR LÉXICO <<</err>\n</body>\n</html>'
            html.write(err_msg.encode('utf8')) # encoding
            html.close()
            sys.exit(1)
            return ERR