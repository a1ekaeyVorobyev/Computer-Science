import lexer
import intrep
import sys


def run_script(tokens: list):
    """Запуск скрипта из файла"""
    interpretator = intrep.Interpretator()
    for token in tokens:
        interpretator.intrep(token)


def load_file(name_file) -> str:
    """Загрузка скрипта из файла"""
    with open(name_file) as file:
        script = file.read()
    return script


def get_token(script: str) -> list:
    """Преобразование скрипта в token"""
    lex_disassembly = lexer.LexDisassembly()
    return lex_disassembly.create_list_tokens(script)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # print("Введите имя скрипта для обработки")
        run_script(get_token(load_file("script.txt")))
    else:
        for param in sys.argv[1:]:
            run_script(get_token(load_file(param)))
