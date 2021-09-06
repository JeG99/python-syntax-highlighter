# <prog> ::= <exp> <prog> | $
# <exp> ::= <átomo> | <lista>
# <átomo> ::= símbolo | <constante>
# <constante> ::= número | booleano | string
# <lista> ::= ( <elementos> )
# <elementos> ::= <exp> <elementos> | epsilon


#
#

# exp():
# atm()
# cons()

# atm():
# elif token == scanner.SYM:
#         match(token)
# const()


import sys
import return_token as scanner


def match(expectedToken):
    global token
    if token == expectedToken:
        token = scanner.get_token()
    else:
        error("Wrong token")

def parser():
    global token
    html = open('index.html', 'w')
    html.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n<link href="style.css" rel="stylesheet" type="text/css">\n</head>\n<body>\n')
    html.close()
    token = scanner.get_token()
    prog()
    html = open('index.html', 'a')
    html.write('</body>\n</html>')
    html.close()

def prog():
    if token == scanner.SYM or token == scanner.NUM or token == scanner.STR or token == scanner.BOO or token == scanner.LRP:
        exp()
        prog()
    else:
        if token == scanner.END:
            print("Expresion bien construida")
        else:
            error("Expresion mal terminada")

def exp():
    if token == scanner.LRP:
        print("Inside exp", token)
        lis()
    else:
        atm()

def atm():
    if token == scanner.SYM:
        match(token)
    else:
        con()

def con():
    if token == scanner.NUM:
        match(token)
    elif token == scanner.BOO:
        match(token)
    elif token == scanner.STR:
        match(token)
    else:
        error("Se esperaba una constante")

def lis():
    match(scanner.LRP)  # reconoce Delimitador (
    ele()
    match(scanner.RRP)

def ele():
    if token == scanner.SYM or token == scanner.NUM or token == scanner.STR or token == scanner.BOO or token == scanner.LRP:
        exp()
        ele()

def error(msg):
    html = open('index.html', 'w')
    html.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n<link href="style.css" rel="stylesheet" type="text/css">\n</head>\n<body>\n<err>ERROR: ' + msg + '</err>\n</body>\n<html>') 
    html.close()
    sys.exit(1)
