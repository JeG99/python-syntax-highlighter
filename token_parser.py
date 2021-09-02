# <prog> ::= <exp> <prog> | $
# <exp> ::= <átomo> | <lista>
# <átomo> ::= símbolo | <constante>
# <constante> ::= número | booleano | string
# <lista> ::= ( <elementos> )
# <elementos> ::= <exp> <elementos> | 

# <prog> ::= <exp> <prog> | $
# <exp> ::= simbolo | número | booleano | string | <lista>
# <lista> ::=
#
#

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
    token = scanner.get_token()
    prog()
    if token == scanner.END:
        print("Expresion bien construida")
    else:
        error("Expresion mal terminada")


def prog():
    exp()


def exp():
    if token == scanner.NUM:
        match(token)
        exp()
    elif token == scanner.STR:
        match(token)
        exp()
    elif token == scanner.BOO:
        match(token)
        exp()
    elif token == scanner.SYM:
        match(token)
        exp()
    elif token == scanner.LRP:
        match(token)
        exp()
        match(scanner.RRP)
        exp()


def deli():
    match(scanner.LRP)
    exp()
    match(scanner.RRP)
    exp()


def error(msg):
    print("ERROR:", msg)
    sys.exit(1)
