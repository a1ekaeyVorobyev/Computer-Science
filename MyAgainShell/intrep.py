dicValue = {}

def is_float(value):
  if value is None:
      return False
  try:
      float(value)
      return True
  except:
      return False

def is_int(value):
    if type(value) is int:
        return True
    if type(value) is str:
        if value is None:
            return False
        if value.isdigit():
            return True
        else:
            return False
    return False

def typeDefinitions(val):
    if val == None:
        return val
    if type(val) is bool:
        return val
    if is_int(val):
        return int(val)
    if is_float(val):
        return float(val)
    if val[0] == '"':
        return val[1:-1:]
    return val

def  assign(val):
    if type(val[2]) is list:
        g = intrep(val[2])
        dicValue[val[1]] = typeDefinitions(g)
    else:
        dicValue[val[1]] = typeDefinitions(val[2])
    return

def add(val):
    val[1] = getValue(val[1])
    val[2] = getValue(val[2])
    return val[1]+val[2]

def sub(val):
    val[1] = getValue(val[1])
    val[2] = getValue(val[2])
    return val[1]-val[2]

def mult(val):
    val[1] = getValue(val[1])
    val[2] = getValue(val[2])
    return val[1]*val[2]

def div(val):
    val[1] = getValue(val[1])
    val[2] = getValue(val[2])
    return val[1]/val[2]


def printValue(val):
    g = getValue(val[1])
    print(g)
    return

def inputValue(val):
    txt = input()
    dicValue[val[1]] = txt
    return

def getValue(val):
    if type(val) is list:
        return intrep(val)
    elif not is_float(val) and val[0] != '"':
        if val in dicValue.keys():
            return dicValue[val]
        else:
            raise MyException('Переменная не обЪявленна')
    return typeDefinitions(val)

def func(val):
    if val[1] in dicValue.keys():
        return funcStr(val)
    else:
        raise MyException('Переменная не обЪявленна') 
    return

def funcStr(val):
    if val[2] == "Upper":
        dicValue[val[1]] = dicValue[val[1]].upper()
        return dicValue[val[1]]
    
    if val[2] == "Lower":
        dicValue[val[1]] = dicValue[val[1]].lower()
        return dicValue[val[1]]
    
    raise MyException('Не такой встроенной функции')

def logOperation(val):
    val[1] = getValue(val[1])
    val[2] = getValue(val[2])
    if val[0] == '==':
        return val[1]==val[2]
    if val[0] == '>=':
        return val[1]>=val[2]
    if val[0] == '<=':
        return val[1]<=val[2]
    if val[0] == '>':
        return val[1]>val[2]
    if val[0] == '<':
        return val[1]<val[2]
    if val[0] == '&&':
        return val[1] and val[2]
    if val[0] == '||':
        return val[1] or val[2]

def func_if (val):
    g = intrep(val[1])
    index=0
    for t in val[2]:
        if t[0] == 'else':
            break
        index+=1
    if g == False and index ==0:
        return
    temp = val[2]
    if g and index > 0:
        temp =  val[2][:index]
    if g == False and index > 0:
        temp =  val[2][index+1:]
    for t in temp:
            intrep(t)
    return

def func_while(val):
    while intrep(val[1]):
        for t in val[2]:
            intrep(t)
    pass

def intrep(value):
    val = value.copy()
    op = val[0]
    ##print(op)
    if op == '=':
        return assign(val)
    if op == '+':
        return add(val)
    if op == '<<':
        return printValue(val)
    if op == '>>':
        return inputValue(val)
    if op == '-':
        return sub(val)
    if op == '*':
        return mult(val)
    if op == '/':
        return div(val)
    if op == '+=' or op == '-=' or op == '*=' or op == '/=':
        t = val.copy()
        t[2] = val
        t[2][0] = t[0][0]
        t[0] = '='
        return assign(t)
    if op == '==' or op =='!=' or op =='>=' or op =='<=' or op =='>' or op =='<' or op =='&&' or op =='||' :
        return logOperation(val)
    if op == ".":
        return func(val)
    if op == "if":
        return func_if(val)
    if op == "while":
        return func_while(val)
    return
