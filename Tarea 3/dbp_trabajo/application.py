from flask import Flask, g, redirect, render_template, request, session, url_for


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'
    
users = []
users.append(User(id=1, username='Victor',password='password'))
users.append(User(id=2, username='Carlos',password='carlos'))


app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('index'))

        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/index')
def index():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('index.html')

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
