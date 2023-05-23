priority = ['&&','||','==','!=','>=','<=','>','<','*','*=','/','/=','+','+=','-','-=',"="]
reservedWords = ['for','int','string','if','while','<<','>>',':'] 
listWords  = priority + reservedWords+['(',')']

listToken = []
levelToken = 0

def formatString(txt:str) -> str:
    """Форматирование строки перед обработкой"""

    global levelToken
    levelToken = 0
    if listToken != []:
        cntPass =len(txt)-len(txt.lstrip())
        if cntPass %4 != 0:
            raise MyException('Отформатируйте текст') 
        levelToken = cntPass//4
        txt = txt.lstrip()
    s = ''
    prev = ''
    index = 0
    for t in txt:
        if t == "\n":
            index +=1
            continue
        if (prev+t) in listWords  and prev !='':
            s+=t
            index +=1
            prev = t
            continue
        if t in listWords  and prev !='':
            s+=" "+t
            index +=1
            prev = t
            continue
        if prev in listWords  and prev !='':
            s+=' '
        index +=1
        s += t
        prev = t
    while "  " in s:
        s= s.replace("  ", " ")
    s = s.rstrip() 

    return s

def getToken(txt:str) -> list:
    """Переводим строку в token"""
    global levelToken
    token = []
    txt = formatString(txt)
    x = txt.split(" ")
    if x[0] == 'else' or x[0] == 'else:':
        listToken[-1][2].append(['else'])
        levelToken +=1
        return []
    if levelToken<len(listToken) and levelToken>0:
        while levelToken<len(listToken):
            listToken[-2][2].append(listToken[-1])
            del listToken[-1]
    if '(' in txt:
        token = buidTokenParenthesis(x)
    if len(x)==0:
        token = token
    if x[0] in reservedWords:
        token = buildTokenRW(x)
    else:
        token = buildToken(x)
    if levelToken > 0 and token != []:
        listToken[-1][2].append(token)
    return token

def buildTokenRW(text:str)->list:
    """Строим token если используеться reservedWords"""
    global levelToken
    if text[0] == 'if':
        buildTokenIF(text)
    if text[0] == 'while':
        buildTokenIF(text)
    if len(text) < 2:
        return text[0]
    if len(text) < 3:
        return [text[0], text[1],'']
    if len(text) == 3:
        return [text[0], text[1],text[2]]
    levelToken += 1
    return []

def buildToken(text)->list:
    """Строим простой token"""
    if len(text) < 1:
        return text[0]
    if len(text) < 3:
        return [text[0], text[1],'']
    for t in priority[::-1]:
        index = 0
        for w in text:
            if w == t:
                if len(text[:index:1])>1:
                    tokenLeft = buildToken(text[:index:])
                else:
                    tokenLeft = text[index-1]
                if len(text[index+1::1])>1:
                    tokenRight = buildToken(text[index+1::])
                else: 
                    tokenRight = text[index+1]
                return [w, tokenLeft,tokenRight]
            index = index + 1
    return []

def buidTokenParenthesis(text)->list:
    """Строим token если есть скобки"""
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
                token = buildToken(t1)
                text[lenText-index-1] = token
                del text[lenText-index:lenText-var[-1]:]
            else:
                del text[lenText-index-1:lenText-var[-1]:]
            del var[-1]
            index = index - (lenText - len(text))
            lenText = len(text)
        index +=1
    return buildToken(text) 

def  buildTokenIF(text:str):
    """Получение token если строка содержит if, while"""
    global list_token
    if text[-1] == ":":
        del text[-1]
    token = buildToken(text[1::])
    listToken.append([text[0],token,[]])

def createListTokens(script:str)->list:
    """Преобразование скрипта в token"""
    global listToken
    tokens = []
    for line in script.split("\n"):
        if line.strip() == '':
            continue
        token = getToken(line)
        if listToken == []:
            tokens.append(token)
        else :
            if  levelToken == 0:
                tokens.append(listToken[-1])
                listToken=[]
                tokens.append(token)
    if listToken != []:
        while len(listToken)>1:
            listToken[-2][2].append(listToken[-1])
            del listToken[-1]
        tokens.append(listToken[-1])
        listToken = []
    return tokens