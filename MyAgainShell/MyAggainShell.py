import tokenize, io
import pprint
import lexur,intrep
import sys

script = ''

def runScript(tokens:list):
    """Запуск скрипта из файла"""
    for token in tokens:
        intrep.intrep(token)

def loadFile(nameFile):
    """Загрузка скрипта из файла"""
    global script
    with open(nameFile) as file:
        script = file.read()

def getToken()->list:
    """Преобразование скрипта в token"""
    return lexur.getTokens(script)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        #print("Введите имя скрипта для обработки")
        loadFile("script.txt")
        runScript(getToken())
    else:
        for param in sys.argv[1:]:
            loadFile(param)
            runScript(getToken())