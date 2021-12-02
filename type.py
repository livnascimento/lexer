import tag

def numerico(Tipo):
    if Tipo == Int['Type'] or Tipo == Float['Type'] or Tipo == Char['Type']:
        return True
    else :
        return False

def max(tipo1, tipo2):
    if not numerico(tipo1) or not numerico(tipo2):
        return None
    elif tipo1 == Float['Type'] or tipo2 == Float['Type']:
        return Float['Type']
    elif tipo1 == Int['Type'] or tipo2 == Int['Type']:
        return Int['Type']
    else:
        return Char['Type']

Int = {'Type':'int', 'type_tag':tag.BASIC, 'width':4}
Float = {'Type':'float', 'type_tag':tag.BASIC, 'width':8}
Char = {'Type':'char', 'type_tag':tag.BASIC, 'width':1}
Bool = {'Type':'boolean', 'type_tag':tag.BASIC, 'width':1}