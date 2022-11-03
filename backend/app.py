# importaciones
from flask import Flask, redirect, render_template , url_for
from src.core import database
from flask_sqlalchemy import SQLAlchemy
from flask_session.__init__ import Session

# creacion de la aplicacion flask
app = Flask(__name__, template_folder='src/web/templates', static_folder='src/web/static')

# configuracion de la bd
app.secret_key= "holamundo"
# Server Side session
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#controllers
from src.web.controllers import auth_controller

# Imports tablas de los modelos
from src.core.models.usuario_model import Usuario

#método index que retorna a una vista  y será el que atienda a las peticiones de la raíz de nuestro servidor.
@app.route("/")
def home():
     return render_template('index.html')

 # Autenticacion
app.add_url_rule('/iniciar_sesion', 'login', auth_controller.login, methods=["GET", "POST"])

if __name__ == '__main__':
    app.run(debug=True)




