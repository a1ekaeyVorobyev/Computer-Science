class LexDisassembly:
    __priority = ['&&', '||', '==', '!=', '>=', '<=', '>', '<', '*', '*=', '/', '/=', '+', '+=', '-', '-=', "="]
    __reservedWords = ['for', 'int', 'string', 'if', 'while', '<<', '>>', ':']
    __listWords = __priority + __reservedWords + ['(', ')']

    __listToken = []
    __levelToken = 0

    def format_string(self, txt: str) -> str:
        """
        Форматирование строки перед обработкой

        Parameters:
            txt(str):
        Return:
            str: Возвращает отформатированную строку для дальнейшего разбора
    """

        self.__levelToken = 0

        cnt_pass = len(txt) - len(txt.lstrip())
        if cnt_pass % 4 != 0:
            raise Exception('Отформатируйте текст')
        self.__levelToken = cnt_pass // 4
        txt = txt.lstrip()

        new_str = ''
        prev_char = ''
        index = 0
        for t in txt:
            if t == "\n":
                index += 1
                continue
            if (prev_char + t) in self.__listWords and prev_char != '':
                new_str += t
                index += 1
                prev_char = t
                continue
            if t in self.__listWords and prev_char != '':
                new_str += '' if (prev_char + t) in self.__listWords else ' ' + t
                index += 1
                prev_char = t
                continue
            if prev_char in self.__listWords and prev_char != '':
                new_str += ' '
            index += 1
            new_str += t
            prev_char = t
        while "  " in new_str:
            new_str = new_str.replace("  ", " ")
        new_str = new_str.rstrip()

        return new_str

    def get_token(self, txt: str):
        """Переводим строку в token

        Parameters:
            txt(str): Строку с кодом
        Return:
            list,None: Возвращаем ее  как token

    """
        txt = self.format_string(txt)
        x = txt.split(" ")
        if x[0].startswith('else'):
            self.__listToken[-1][2].append(['else'])
            self.__levelToken += 1
            return []
        if len(self.__listToken) > self.__levelToken > 0:
            while self.__levelToken < len(self.__listToken):
                self.__listToken[-2][2].append(self.__listToken[-1])
                del self.__listToken[-1]
        if '(' in txt:
            token = self.build_token_parenthesis(x)
            return token
        if x[0] in self.__reservedWords:
            token = self.build_token_rw(x)
        else:
            token = self.build_token(x)
        if self.__levelToken > 0 and token != []:
            self.__listToken[-1][2].append(token)
        return token

    def build_token_rw(self, text: str) -> list:
        """Строим token если используется reservedWords

        Parameters:
            txt(str): Строку с кодом
        Return:
            list: Возврашаем ее  как token
    """
        if text[0] == 'if':
            self.build_token_if(text)
        if text[0] == 'while':
            self.build_token_if(text)
        if len(text) < 2:
            return text[0]
        if len(text) < 3:
            return [text[0], text[1], '']
        if len(text) == 3:
            return [text[0], text[1], text[2]]
        self.__levelToken += 1
        return []

    def build_token(self, text) -> list:
        """Строим простой token

        Parameters:
            txt(str): Строку с кодом
        Return:
            list: Возврашаем ее  как token
    """
        if len(text) < 1:
            return text[0]
        if len(text) < 3:
            return [text[0], text[1], '']
        for word_priority in self.__priority[::-1]:
            index = 0
            for word in text:
                if word == word_priority:
                    if len(text[:index:1]) > 1:
                        token_left = self.build_token(text[:index:])
                    else:
                        token_left = text[index - 1]
                    if len(text[index + 1::1]) > 1:
                        token_right = self.build_token(text[index + 1::])
                    else:
                        token_right = text[index + 1]
                    return [word, token_left, token_right]
                index += 1
        return []

    def build_token_parenthesis(self, text) -> list:
        """Строим token если есть скобки

        Parameters:
            txt(str): Строку с кодом
        Return:
            list: Возврашаем ее  как token
    """
        list_parenthesis = []
        index = 0
        len_text = len(text)
        for t in text[::-1]:
            if "." in t:
                x = t.split('.')
                token = ['.', x[0], x[1]]
                text[len_text - index - 1] = token
                continue
            if ")" in t:
                list_parenthesis.append(index)
            if "(" in t:
                if not list_parenthesis:
                    raise Exception('Ошибка в синтаксисе ()')
                t1 = text[len_text - index:len_text - list_parenthesis[-1] - 1:]
                if len(t1) > 1:
                    token = self.build_token(t1)
                    text[len_text - index - 1] = token
                    del text[len_text - index:len_text - list_parenthesis[-1]:]
                else:
                    del text[len_text - index - 1:len_text - list_parenthesis[-1]:]
                del list_parenthesis[-1]
                index = index - (len_text - len(text))
                len_text = len(text)
            index += 1
        if list_parenthesis:
            raise Exception('Ошибка в синтаксисе ()')
        return self.build_token(text)

    def build_token_if(self, text: str) -> None:
        """Получение token если строка содержит if, while

        Parameters:
            txt(str): Строку переводим в token и  добавляем в словарь

    """
        if text[-1] == ":":
            del text[-1]
        token = self.build_token(text[1::])
        self.__listToken.append([text[0], token, []])

    def create_list_tokens(self, script: str) -> list:
        """Преобразование скрипта в token

        Parameters:
            txt(str): скрипт
        Return:
            list: Возврашаем список token
    """
        tokens = []
        for line in script.split("\n"):
            if line.strip() == '':
                continue
            token = self.get_token(line)
            if not self.__listToken:
                tokens.append(token)
            else:
                if self.__levelToken == 0:
                    tokens.append(self.__listToken[-1])
                    self.__listToken = []
                    tokens.append(token)
        if self.__listToken:
            while len(self.__listToken) > 1:
                self.__listToken[-2][2].append(self.__listToken[-1])
                del self.__listToken[-1]
            tokens.append(self.__listToken[-1])
            self.__listToken = []
        return tokens

    def __init__(self):
        __listToken = []
        __levelToken = 0
