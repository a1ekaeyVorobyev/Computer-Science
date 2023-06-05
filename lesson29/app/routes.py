from flask import flash, redirect, render_template, request
from app import app
import lexer
import intrep


@app.route('/')
@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        try:
            script = request.form.get("script")
            lex_disassembly = lexer.LexDisassembly()
            tokens = lex_disassembly.create_list_tokens(script)
            str_token = '\n'.join(map(str, tokens))
            interpretator = intrep.Interpretator()
            for token in tokens:
                interpretator.intrep(token)

            return render_template(
                "indexResponse.html",
                title="Main Page",
                script=script,
                token=str_token,
                result=interpretator.get_result(),
            )
        except:
            return 'Не удалось выполнить скрипт.'
    return render_template(
        "index.html",
        title="Main Page",
        script="""a = 2
while a<100:
    a+=1
<<a""",
        # revText = pythonText[::-1],
    )


@app.route('/exec')
def query_example():
    # if key doesn't exist, returns None
    try:
        script = request.args.get('query')
        script = script.strip()
        lex_disassembly = lexer.LexDisassembly()
        tokens = lex_disassembly.create_list_tokens(script)
        str_token = '\n'.join(map(str, tokens))
        interpretator = intrep.Interpretator()
        for token in tokens:
            interpretator.intrep(token)

        return render_template(
            "indexResponse.html",
            title="Main Page",
            script=script,
            token=str_token,
            result=interpretator.get_result(),
        )
    except:
        return 'Не удалось выполнить скрипт.'
