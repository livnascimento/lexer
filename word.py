from token import new_token
import tag

palavras_reservadas = {'and':{'string': '&&', 'tag': tag.AND}, 'eq':{'string':'==', 'tag':tag.EQ},'le':{'string':'<=', 'tag':tag.LE},'minus':{'string':'minus', 'tag':tag.MINUS},'False':{'string':'false', 'tag':tag.FALSE},'or':{'string':'||', 'tag':tag.OR},'ne':{'string':'!=', 'tag':tag.NE},'ge':{'string':'>=', 'tag':tag.GE},'True':{'string':'true', 'tag':tag.TRUE},'temp':{'string':'t', 'tag':tag.TEMP}}