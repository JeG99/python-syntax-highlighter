import sys

SYM = 100 # SYMBOL
NUM = 200 # NUMBER
BOO = 300 # BOOLEAN
STR = 400 # STRING
LRP = 501 # LEFT PARENTHESIS
RRP = 502 # RIGHT PARENTHESIS
END = 600 # END
ERR = 700 # ERROR

#      a-z 0-9   #   " t/f spc  \n   (   ) rar   $       
MT = [[  1,  2,  3,  4,  1,  0,  0,LRP,RRP,  7,END], # 0 -> Intial State
      [  1,  7,  7,  7,  7,SYM,SYM,LRP,RRP,  7,  7], # 1 -> Symbol 
      [  7,  2,  7,  7,  7,NUM,NUM,  7,  7,  7,  7], # 2 -> Number
      [  7,  7,  7,  4,  7,ERR,  7,  7,  7,  7,  7], # 3 -> # of Bool
      [  7,  7,  7,  7,  7,BOO,BOO,  7,  7,  7,  7], # 4 -> t/f of Bool
      [  5,  5,  7,  6,  7,  5,  7,  7,  7,  7,  7], # 5 -> String Char
      [  7,  7,  7,  7,  7,STR,STR,LRP,RRP,  7,  7], # 6 -> Closing quotes String
      [  7,  7,  7,  7,  7,ERR,  7,  7,  7,  7,  7]] # 7 ->   7or state

      #Porque se loopea estado de error?

def filter(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'): # a-z
        return 0
    elif c == '0' or c == '1' or c == '2' or \
         c == '3' or c == '4' or c == '5' or \
         c == '6' or c == '7' or c == '8' or c == '9': # 0-9
        return 1
    elif c == '#': # hashtag
        return 2
    elif c == '"': # Quote
        return 3
    elif c == 't' or c =='f': # true of false
        return 4
    elif c == ' ': # blank space 
        return 5
    elif c == '\n': # new line
        return 6
    elif c == '(': # delimitator (
        return 7  
    elif c == ')': # delimiator ) 
        return 8
    elif c == '$': # End 
        return 10
    else:         # Rare char
        return 9 

_c = None
_read = True

def get_token():
    global _c, _read
    state = 0
    lexeme = ""
    
    while(True):
        while state < 100:
            if _read: 
                _c = sys.stdin.read(1)
            else: _read = True
            state = MT[state][filter(_c)]
            if state < 100 and state != 0: lexeme += _c
        if state == SYM:
            _read = False
            print("Symbol", lexeme)
            return SYM
        elif state == NUM:
            _read = False
            print("Number", lexeme)
            return NUM
        elif state == BOO:
            _read = False
            print("Boolean", lexeme)
            return BOO
        elif state == STR:
            _read = False
            print("String", lexeme)
            return STR
        elif state == LRP:
            _read = False
            print("Delimitator", lexeme)
            return LRP
        elif state == RRP:
            _read = False
            print("Delimitator", lexeme)
            return RRP
        elif state == END:
            print("Fin de expresion")
            return END
        else:
            _read = False
            print("Error, not accepted word", lexeme)
            return ERR

        