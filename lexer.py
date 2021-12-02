from Python3.lexer.token import new_token
import type
import tag
import token
import word

line = 1
peek = ' '
words = {} # dictionary substituindo hashtable
w_num = -1

def reserva(p):
    global w_num
    w_num = w_num + 1
    words['lexeme'+ w_num] = new_token(s=p,t=p)

def lerLetra():
    peek = input()

def lerLetra(c):
    lerLetra()
    global peek
    if peek != c :
        return False
    peek = ' '
    return True

def scan():
    while lerLetra():
        if peek == ' ' or peek == '\t':
            continue
        elif peek == '\n':
            line = line + 1
        else: 
            break
    
    if peek == '&':
        if lerLetra() == '&':
            return word.palavras_reservadas['and']
        else:
            words['lexeme' + (w_num + 1)] = new_token(s='&', t='&')
