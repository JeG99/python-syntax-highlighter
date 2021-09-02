# <prog> ::= <exp> <prog> | $
# <exp> ::= <átomo> | <lista>
# <átomo> ::= símbolo | <constante>
# <constante> ::= número | booleano | string
# <lista> ::= ( <elementos> )
# <elementos> ::= <exp> <elementos> | epsilon

# <prog> ::= <exp> <prog> | $
# <exp> ::= simbolo | número | booleano | string | <lista>
# <lista> ::=
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
    token = scanner.get_token()
    prog()


def prog():
    if token == scanner.SYM or token == scanner.NUM or token == scanner.STR or token == scanner.BOO or token == scanner.LRP or token == scanner.RRP:
        exp()
        prog()
    else:
        if token == scanner.END:
            print("Expresion bien construida")
        else:
            error("Expresion mal terminada")


def exp():
    if token == scanner.LRP or token == scanner.RRP:
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


def lis():
    if token == scanner.LRP:
        match(token)  # reconoce Delimitador (
        ele()
        match(scanner.RRP)


def ele():
    exp()
    ele()


def error(msg):
    print("ERROR:", msg)
    sys.exit(1)
