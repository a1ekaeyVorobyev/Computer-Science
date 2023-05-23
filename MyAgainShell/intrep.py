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

def add(val:list):
    """Функция сложения"""
    val[1] = getValue(val[1])
    val[2] = getValue(val[2])
    return val[1]+val[2]

def sub(val:list):
    """Функция вычетания"""
    val[1] = getValue(val[1])
    val[2] = getValue(val[2])
    return val[1]-val[2]

def mult(val:list):
    """Функция умножения"""
    val[1] = getValue(val[1])
    val[2] = getValue(val[2])
    return val[1]*val[2]

def div(val:list):
    """Функция деления"""
    val[1] = getValue(val[1])
    val[2] = getValue(val[2])
    return val[1]/val[2]


def printValue(val:list):
    """Вывод на экран"""
    value = getValue(val[1])
    print(value)

def inputValue(val:list):
    """Вывод значения"""
    dicValue[val[1]] = input()

def getValue(val:str):
    """Получения значения"""
    if type(val) is list:
        return intrep(val)
    elif not is_float(val) and val[0] != '"':
        if val in dicValue.keys():
            return dicValue[val]
        else:
            raise MyException('Переменная не обЪявленна')
    return typeDefinitions(val)

def func(val:list):
    """определение, функции после точки"""
    if val[1] in dicValue.keys():
        return funcStr(val)
    else:
        raise MyException('Переменная не обЪявленна') 
    return

def funcStr(val:list)->str:
    """Встроенные функции над строкой"""
    if val[2] == "Upper":
        dicValue[val[1]] = dicValue[val[1]].upper()
        return dicValue[val[1]]
    
    if val[2] == "Lower":
        dicValue[val[1]] = dicValue[val[1]].lower()
        return dicValue[val[1]]
    
    raise MyException('Не такой встроенной функции')

def logOperation(val:list)->bool:
    """выполнение логически операторов"""
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

def funcIF (val:list):
    """Выполнение token IF"""
    value = intrep(val[1])
    index=0
    for t in val[2]:
        if t[0] == 'else':
            break
        index+=1
    if value == False and index ==0:
        return
    temp = val[2]
    if value and index > 0:
        temp =  val[2][:index]
    if value == False and index > 0:
        temp =  val[2][index+1:]
    for t in temp:
            intrep(t)

def funcWhile(val:list):
    """Выполнение token while"""
    while intrep(val[1]):
        for value in val[2]:
            intrep(value)

def intrep(value:list):
    """Интрепретатор"""
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
        return funcIF(val)
    if op == "while":
        return funcWhile(val)
    return
