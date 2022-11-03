# importaciones
from datetime import datetime
from src.core.database import db

#clase Usuario(tabla)
class Usuario(db.Model):
    
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(500))    
    email = db.Column(db.String(50))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    activo = db.Column(db.String(10)) #activo no-activo
    inserted_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now())


    # def __init__(
    #         self, email, username, password, first_name, last_name
    # ):
    #     self.email = email
    #     self.username = username
    #     self.password = password
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.activo = "Activo"

    # def __repr__(self):
    #     return "<user(username='%s',email='%s', first_name='%s', last_name='%s' )>" % (
    #         self.username,
    #         self.email,
    #         self.first_name,
    #         self.last_name,
    #     )

    # #listar usuarios de la bd sin paginacion
    # def list_usuarios():
    #     return Usuario.query.all()

    # @classmethod
    # def get_estado_activo(self):
    #     return "Activo"

    # @classmethod
    # def get_estado_no_activo(self):
    #     return "Desactivo"
    
    # @classmethod
    # def get_user_by_id(self, user_id):
    #     return Usuario.query.filter(self.id == user_id).first()            
        
    # @classmethod
    # def get_user_by_username_and_password(self, username, password):
    #     return Usuario.query.filter(self.username == username, self.password == password).first()

    # @classmethod
    # def get_user_by_username(self, username):
    #     return Usuario.query.filter(self.username == username).first()

