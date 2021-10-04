from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        resumen = request.form.get("resumen")
        datosperso = request.form.get("datosperso")
        experiencia = request.form.get("experiencia")
        estudios = request.form.get("estudios")
        logros = request.form.get("logros")
        habilidades = request.form.get("habilidades")
        intereses = request.form.get("intereses")
        referencias = request.form.get("referencias")
        return render_template("hello.html", nombre=nombre,resumen=resumen,datosperso=datosperso,experiencia=experiencia,estudios=estudios,logros=logros,habilidades=habilidades,intereses=intereses,referencias=referencias)
