priority = ['&&','||','==','!=','>=','<=','>','<','*','*=','/','/=','+','+=','-','-=',"="]
reserved_words = ['for','int','string','if','while','<<','>>',':'] 
list_words  = priority + reserved_words+['(',')']

list_token = []
level_list_token = []
level_token = 0

def  getToken(txt):
    global level_token
    token = []
    level_token = 0
    if list_token != []:
        cntPass =len(txt)-len(txt.lstrip())
        if cntPass %4 != 0:
            raise MyException('Отформатируйте текст') 
        level_token = cntPass//4
        txt = txt.lstrip()
    s = ''
    prev = ''
    index = 0
    for t in txt:
        if t == "\n":
            index +=1
            continue
        if (prev+t) in list_words  and prev !='':
            s+=t
            index +=1
            prev = t
            continue
        if t in list_words  and prev !='':
            s+=" "+t
            index +=1
            prev = t
            continue
        if prev in list_words  and prev !='':
            s+=' '
        index +=1
        s += t
        prev = t
    while "  " in s:
        s= s.replace("  ", " ")
    s = s.rstrip() 
    x = s.split(" ")
    if x[0] == 'else' or x[0] == 'else:':
        level_list_token[-1][2].append(['else'])
        level_token +=1
        return []
    if level_token<len(level_list_token) and level_token>0:
        while level_token<len(level_list_token):
            level_list_token[-2][2].append(level_list_token[-1])
            del level_list_token[-1]
    if '(' in s:
        token = buid_token_parenthesis(x)
    if len(x)==0:
        token = token
    if x[0] in reserved_words:
        token = build_token_rw(x)
    else:
        token = build_token(x)
    if level_token > 0 and token != []:
        level_list_token[-1][2].append(token)
    return token

def build_token_rw(text):
    global level_token
    if text[0] == 'if':
        build_token_if(text)
    if text[0] == 'while':
        build_token_if(text)
    if len(text) < 2:
        return text[0]
    if len(text) < 3:
        return [text[0], text[1],'']
    if len(text) == 3:
        return [text[0], text[1],text[2]]
    level_token += 1
    return []

def build_token(text):
    if len(text) < 1:
        return text[0]
    if len(text) < 3:
        return [text[0], text[1],'']
    for t in priority[::-1]:
        index = 0
        for w in text:
            if w == t:
                if len(text[:index:1])>1:
                    tokenLeft = build_token(text[:index:])
                else:
                    tokenLeft = text[index-1]
                if len(text[index+1::1])>1:
                    tokenRight = build_token(text[index+1::])
                else: 
                    tokenRight = text[index+1]
                return [w, tokenLeft,tokenRight]
            index = index + 1
    return []

def buid_token_parenthesis(text):
    var = []
    index = 0
    lenText = len(text)
    for t in text[::-1]:
        if "." in t:
            x = t.split('.')
            token = ['.',x[0],x[1]]
            text[lenText-index-1] = token
            continue
        if ")" in t:
            var.append(index)
        if "(" in t:
            t1 = text[lenText-index:lenText-var[-1]-1:]
            if len(t1)>1:
                token = build_token(t1)
                text[lenText-index-1] = token
                del text[lenText-index:lenText-var[-1]:]
            else:
                del text[lenText-index-1:lenText-var[-1]:]
            del var[-1]
        index +=1
    return build_token(text) 

def  build_token_if(text):
    global list_token
    if text[-1] == ":":
        del text[-1]
    token = build_token(text[1::])
    level_list_token.append([text[0],token,[]])
    if level_token == 0:
        list_token = level_list_token[-1]
    pass


