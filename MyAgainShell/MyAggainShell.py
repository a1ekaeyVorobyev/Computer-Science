import tokenize, io
import pprint
import lexur,intrep
import sys

tokens = []
script = ''

def runScript():
    for token in tokens:
        intrep.intrep(token)

def loadFile(nameFile):
    global script
    with open(nameFile) as file:
        script = file.read()

def getToken():
    for line in script.split("\n"):
        if line.strip() == '':
            continue
        r = lexur.getToken(line)
        if lexur.list_token == []:
            tokens.append(r)
        else :
            if  lexur.level_token == 0:
                tokens.append(lexur.list_token)
                lexur.list_token=[]
                tokens.append(r)
    if lexur.list_token != []:
        tokens.append(lexur.list_token)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        #print("Введите имя скрипта для обработки")
        loadFile("script.txt")
        getToken()
        runScript()
    else:
        for param in sys.argv[1:]:
            loadFile(param)
            getToken()
            runScript()