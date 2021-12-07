from token1 import new_token
from num import new_num
from real import new_real
from tag import *
from word import *
import time

line = 0
letra_ind = 0
peek = ' '
words = {} # dictionary substituindo hashtable
w_num = 0

arquivo = open('/home/joao/Documentos/códigos/Python3/lexer/test.txt')
conteudo = arquivo.readlines()
arquivo.close()

def reserva(p):
    global w_num
    words['lexeme'+ str(w_num)] = new_token(s=p,t=p)
    w_num += 1

def lerLetra():
    global peek
    global letra_ind
    print(peek)
    peek = conteudo[line][letra_ind]
    time.sleep(1)
    if letra_ind < len(conteudo[line]) -1:
        letra_ind += 1
    elif letra_ind == len(conteudo[line]) -1:
        return True

def lerletter(letra):
    lerLetra()
    global peek
    if peek != letra :
        return False
    peek = ' '
    return True

def scan():
    while lerLetra():
        if peek == ' ' or peek == '\t':
            continue
        elif peek == '\n':
            global letra_ind
            global line
            line += 1
            letra_ind = 0
        elif lerLetra() == '':
            return None
    
    if peek == '&':
        if lerletter('&'):
            return palavras_reservadas['and']
        else:
            global w_num
            w_num += 1
            words['lexeme' + str(w_num)] = new_token(s='&', t='&')
            return words['lexeme' + str(w_num)]

    elif peek == '|':
        if lerletter('|'):
            return palavras_reservadas['or']
        else:
            w_num += 1
            words['lexeme' + str(w_num)] = new_token(s='|', t='|')
            return words['lexeme' + str(w_num)]

    elif peek == '=':
        if lerletter('='):
            return palavras_reservadas['eq']
        else:
            w_num += 1
            words['lexeme' + str(w_num)] = new_token(s='=', t='=')
            return words['lexeme' + str(w_num)]

    elif peek == '!':
        if lerletter('='):
            return palavras_reservadas['ne']
        else:
            w_num += 1
            words['lexeme' + str(w_num)] = new_token(s='!', t='!')
            return words['lexeme' + str(w_num)]

    elif peek == '<':
        if lerletter('='):
            return palavras_reservadas['le']
        else:
            w_num += 1
            words['lexeme' + str(w_num)] = new_token(s='<', t='<')
            return words['lexeme' + str(w_num)]

    elif peek == '>':
        if lerletter('='):
            return palavras_reservadas['ge']
        else:
            w_num += 1
            words['lexeme' + str(w_num)] = new_token(s='>', t='>')
            return words['lexeme' + str(w_num)]
    

    if peek.isdigit():
        v = 0
        while True:
            v = 10*v + int(peek)
            lerLetra()
            if(not peek.isdigit()):
                break

        if(peek != '.'):
            return new_num(v)

        x = v
        d = 10

        while(True):
            lerLetra()
            if not peek.isalpha():
                break
            x = x + int(peek)/d
            d = d * 10
        
        return new_real(x)

    if peek.isalpha():
        buffer = []
        while True:
            buffer.append(peek)
            lerLetra()
            if not peek.isalnum():
                break

        palavra = ''
        
        for letter in buffer:
            palavra += letter
        
        if palavra != '':
            return palavra
        
        words[palavra] = {'string':palavra, 'tag':tag.ID}
        return {'string':palavra, 'tag':tag.ID}

    w_num += 1
    words['lexeme' + str(w_num)] = new_token(s=peek,t=peek)
    return words['lexeme' + str(w_num)]

