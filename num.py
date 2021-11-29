import tag, token

def cria(v):
  numero = token.cria(tag.num)
  numero['value'] = v
  return numero 
