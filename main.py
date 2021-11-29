from lexer import lexer
from parser import parser

def main():

    lex = lexer()
    parse = parser(lex)

main()