from num import new_num
from real import new_real
from token import new_token
import tag
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

def lerLetra(letra):
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
            line = line + 1
        else: 
            break
    
    if peek == '&':
        if lerLetra('&'):
            return word.palavras_reservadas['and']
        else:
            global w_num
            w_num += 1
            words['lexeme' + w_num] = new_token(s='&', t='&')
            return words['lexeme' + w_num]
    elif peek == '|':
        if lerLetra('|'):
            return word.palavras_reservadas['or']
        else:
            global w_num
            w_num += 1
            words['lexeme' + w_num] = new_token(s='|', t='|')
            return words['lexeme' + w_num]
    elif peek == '=':
        if lerLetra('='):
            return word.palavras_reservadas['eq']
        else:
            global w_num
            w_num += 1
            words['lexeme' + w_num] = new_token(s='=', t='=')
            return words['lexeme' + w_num]
    elif peek == '!':
        if lerLetra('!'):
            return word.palavras_reservadas['ne']
        else:
            global w_num
            w_num += 1
            words['lexeme' + w_num] = new_token(s='!', t='!')
            return words['lexeme' + w_num]
    elif peek == '<':
        if lerLetra('<'):
            return word.palavras_reservadas['le']
        else:
            global w_num
            w_num += 1
            words['lexeme' + w_num] = new_token(s='<', t='<')
            return words['lexeme' + w_num]
    elif peek == '>':
        if lerLetra('>'):
            return word.palavras_reservadas['ge']
        else:
            global w_num
            w_num += 1
            words['lexeme' + w_num] = new_token(s='>', t='>')
            return words['lexeme' + w_num]
    
    if peek.isdigit():
        v = 0

        while True:
            v = 10*v + (int(peek))
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
            palavra = palavra + letter
        
        if palavra != None:
            return palavra
        
        words[palavra] = {'string':palavra, 'tag':tag.ID}
        return {'string':palavra, 'tag':tag.ID}

    w_num += 1
    words['lexeme' + w_num] = new_token(s=peek,t=peek)
    return words['lexeme' + w_num]