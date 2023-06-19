class Interpretator:
    __dicValue = {}
    __str_output = ''

    def is_float(self, value) -> bool:
        '''
        является ли значение float

        Parameters:
            val(str,int,float,bool):
        Return:
            True/False:
    '''
        if value is None:
            return False
        try:
            float(value)
            return True
        except:
            return False

    def is_int(self, value):
        '''
        является ли значение int

        Parameters:
            val(str,int,float,bool):
        Return:
            True/False:
    '''
        if type(value) is int:
            return True
        if type(value) is str:
            return value.isdigit()
        return False

    def type_definitions(self, val):
        '''
        преобразует в возможный тип

        Parameters:
            val(str,int,float,bool):
        Return:
            str,int,float,bool:
    '''
        if val == None:
            return val
        if type(val) is bool:
            return val
        if self.is_int(val):
            return int(val)
        if self.is_float(val):
            return float(val)
        if val[0] == '"':
            return val[1:-1:]
        return val

    def assign(self, val) -> None:
        '''
    Добавляем переменную в словарь.
        Parameters:
            val(list):

    for example ['=','a','2']
    A variable '2' is placed in the dictionary '__dicValue' by the key 'a'
    '''
        if type(val[2]) is list:
            self.__dicValue[val[1]] = self.type_definitions(self.intrep(val[2]))
        else:
            self.__dicValue[val[1]] = self.type_definitions(val[2])
        return

    def print_value(self, val: list):
        '''
    print variable.
        Parameters:
            val(list):

    for example ['<<','2',''] displaying the value 2
    '''
        value = self.get_value(val[1])
        # print(value)
        self.__str_output = self.__str_output + str(value) + '\n'

    def input_value(self, val: list):
        '''
    input variable.
        Parameters:
            val(list):

    for example ['<<','a',''] move the value entered into the dictionary '__dicValue' by the key 'a'
    '''
        self.__dicValue[val[1]] = input()

    def get_value(self, val: str):
        """
        Получение значения из словаря

        Parameters:
            val(str): значение ключа
        Result:
            int,float,str,bool
    """
        if type(val) is list:
            return self.intrep(val)
        elif not self.is_float(val) and val[0] != '"':
            if val in self.__dicValue.keys():
                return self.__dicValue[val]
            else:
                raise Exception('Переменная не объявлена')
        return self.type_definitions(val)

    def func(self, val: list) -> None:
        """
        определение функции после точки

        Parameters:
            val(list):  ['.', 't', 'Upper']

    """
        if val[1] in self.__dicValue.keys():
            return self.func_str(val)
        else:
            raise Exception('Переменная не обЪявлена')
        return

    def func_str(self, val: list) -> str:
        """
        Встроенные функции над строкой

        Parameters:
            val(list): Для примера ['.', 't', 'Upper']
        Return:
            str    
    """

        dic_func_str = {'Upper': lambda x: x.upper(), 'Lower': lambda x: x.lower()}

        if val[2] in dic_func_str:
            self.__dicValue[val[1]] = dic_func_str[val[2]](self.__dicValue[val[1]])
            return self.__dicValue[val[1]]
        raise Exception('Нет такой встроенной функции')

    def check_variable(self, name_variable: str) -> bool:
        """
        Проверка наличия переменной
        
        Parameters:
            name_variable(list): Проверяем, есть ли такая переменная
        Return:
            True/False 
    """
        return name_variable in self.__dicValue

    def operation_simple(self, val: list):
        """
        Выполнение логических операторов
        
        Parameters:
            val(list): Для примера ['+', '1', '2'] или ['>', '1', '2']
        Return:
            str,int,flat,bool   
        
    """
        dic_operation = {'==': lambda x, y: x == y, '!=': lambda x, y: x != y, '>=': lambda x, y: x >= y,
                         '<=': lambda x, y: x <= y,
                         '>': lambda x, y: x > y, '<': lambda x, y: x < y, '&&': lambda x, y: x and y,
                         '||': lambda x, y: x or y,
                         '+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y,
                         '/': lambda x, y: x / y}

        val[1] = self.get_value(val[1])
        val[2] = self.get_value(val[2])

        if val[0] in dic_operation:
            return dic_operation[val[0]](val[1], val[2])
        raise Exception('Нет такой логической функции')

    def operation(self, val: list):
        """
        Выполнение операторов

        Parameters:
            val(list): Для примера ['if', ['>','a','10'], ['+=','b','2']] 
        Return:
            str,int,flat,bool   
    
    """
        dic_operation = {'if': lambda x: self.func_if(x), 'while': lambda x: self.func_while(x)}

        if val[0] in dic_operation:
            return dic_operation[val[0]](val)
        raise Exception('Нет такой функции')

    def func_if(self, val: list):
        """
        Выполнение оператора if

        Parameters:
            val(list): Для примера ['if', ['>','a','10'], ['+=','b','2'],['else:','',''],[]]
        Return:
            str,int,flat,bool   
    """

        value = self.intrep(val[1])
        index = 0
        for token in val[2]:
            if token[0] == 'else':
                break
            index += 1
        if not value and index == 0:
            return
        tokens = val[2]
        if value and index > 0:
            tokens = val[2][:index]
        if not value and index > 0:
            tokens = val[2][index + 1:]
        for token in tokens:
            self.intrep(token)

    def func_while(self, val: list):
        """
        Выполнение оператора while

        Parameters:
            val(list): Для примера ['while', ['>','a','100'], ['+=','a','2']] 
        Return:
            str,int,flat,bool   
    """
        while self.intrep(val[1]):
            for value in val[2]:
                self.intrep(value)

    def intrep(self, value: list):
        """
        Интрепретатор

        Parameters:
            val(list): Для примера [['=','a','1'],['while', ['>','a','100'], ['+=','a','2']]] 
        Return:
            str,int,flat,bool   
   
    """
        list_operation_simple = ['==', '!=', '>=', '<=', '>', '<', '&&',
                                 '||', '+', '-', '*', '/']
        list_operation = ['if', 'while']
        val = value.copy()
        op = val[0]

        if op == '=':
            return self.assign(val)
        if op == '<<':
            return self.print_value(val)
        if op == '>>':
            return self.input_value(val)  # [+= a 10] [= a [+ a 10]]

        if op == '+=' or op == '-=' or op == '*=' or op == '/=':
            token = val.copy()
            token[2] = val
            token[2][0] = token[0][0]
            token[0] = '='
            return self.assign(token)
        if op in list_operation_simple:
            return self.operation_simple(val)

        if op == ".":
            return self.func(val)

        if op in list_operation:
            return self.operation(val)

        raise Exception('Не найдена операция')
        return

    def get_result(self) -> str:
        str_output = 'Вывод на консоль:\n' + self.__str_output + '\n'
        str_output = str_output + 'Значение переменных:\n'
        for key, value in self.__dicValue.items():
            str_output = str_output + 'Переменная: ' + str(key) + ' Значение: ' + str(value) + '\n'
        return str_output
