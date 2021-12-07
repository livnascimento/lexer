def new_token(s,t):
    try:
        dic = {'string':s, 'tag': int(t)}
    except:
        dic = {'string':s, 'tag': ''}
    return dic