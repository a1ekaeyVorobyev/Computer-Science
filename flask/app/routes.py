from flask import flash, redirect, render_template,request, jsonify
from app import app
from flask import Flask

def validate_post_data(data: dict) -> bool:
    if not isinstance(data, dict):
        return False
    if not data.get('name') or not isinstance(data['name'], str):
        return False
    if data.get('age') and not isinstance(data['age'], int):
        return False
    return True

@app.route('/')
@app.route("/index", methods=['GET', 'POST'])
def index():
    pythonText = ""
    if request.method == "POST":
       # getting input with name = fname in HTML form
        pythonText = request.form.get("pythonText")
        return "Вы ввели: "+pythonText+ " получили:"+pythonText[::-1]
    
    return render_template(
    "index.html", 
    title="Main Page",
    #revText = pythonText[::-1], 
    )


@app.route('/test', methods=['GET'])
def hello():
    return 'Hello World!'

@app.route("/page")
def page2():

    return render_template(
        "page.html",
        title="Second page",
        page="second", 
    )

@app.route('/api', methods=['GET', 'POST'])
def api():
    """
    /api entpoint
    GET - returns json= {'status': 'test'}
    POST -  {
            name - str not null
            age - int optional
            }
    :return:
    """
    if request.method == 'GET':
        return jsonify({'status': 'test'})
    elif request.method == 'POST':
        if validate_post_data(request.json):
            return jsonify({'status': 'OK'})
        else:
            return jsonify({'status': 'bad input'}), 400
