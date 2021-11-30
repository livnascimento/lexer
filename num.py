import tag, token

def create(v):
  number = token.create(tag.NUM)
  number['value'] = v
  return number #{'tag': 270, 'value': }
