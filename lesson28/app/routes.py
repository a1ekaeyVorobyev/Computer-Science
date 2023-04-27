from flask import flash, redirect, render_template,request
from app import app

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


@app.route("/page")
def page2():

    return render_template(
        "page.html",
        title="Second page",
        page="second", 
    )
