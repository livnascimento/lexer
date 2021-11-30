import tag.py

words_reserved = {'and':{'string': '&&', 'tag':tag.AND}, 'eq':{'string':'==', 'tag':tag.EQ},'le':{'string':'<=', 'tag':tag.LE},'minus':{'string':'minus', 'tag':tag.MINUS},'False':{'string':'false', 'tag':tag.FALSE},'or':{'string':'||', 'tag':tag.OR},'ne':{'string':'!=', 'tag':tag.NE},'ge':{'string':'>=', 'tag':tag.GE},'True':{'string':'true', 'tag':tag.TRUE},'temp':{'string':'t', 'tag':tag.TEMP}}

def word(string, tag):
    return {'string':string, 'tag':tag}