# coding: utf-8
from flask import jsonify
from flask.helpers import make_response
from flask.templating import render_template
from flask_login import fresh_login_required, current_user, login_required
from flask_mail import Message
from flask_security.decorators import roles_required

from consultoria.models.treino import Treino, TreinoSchema
from consultoria.modules import mail

from ..modules import db, admin_permission


class TreinoController:
    
    @admin_permission.require(http_exception=403)
    def salvar(self, data): 
        treino, errors= TreinoSchema().load(data)
        treino.usuario_id = data['usuario_id']
        if errors.__len__() > 0 :
            return make_response("Dado de %s inválido" % treino.errors[-1], 500)        
        db.session.add(treino)
        db.session.commit()
        return make_response("Dúvida adicionada com sucesso", 200)
        
    @admin_permission.require(http_exception=403)
    def listar_admin(self):
        schema = TreinoSchema()
        lista = Treino().query.filter().all()        
        return schema.jsonify(lista, True)

    @login_required
    def listar(self):
        schema = TreinoSchema()
        lista = Treino().query.filter(Treino.usuario_id == current_user.id).all()        
        return schema.jsonify(lista, True)
    
    @login_required
    def buscar(self, id):
        return TreinoSchema().jsonify(Treino.query.get(id))
    
    @admin_permission.require(http_exception=403)
    def admin_editar(self, data):
        with db.session.no_autoflush:
            schema = TreinoSchema().load(data, instance=Treino().query.get(data['id']), partial=True)        
            if schema.errors.__len__() > 0:
                return make_response(schema.errors[0], 500)        
            treino = schema.data
            treino.status = 'ativa'
            db.session.add(treino)
            db.session.commit()
            self.emailLiberacaoTreino(treino)
            return TreinoSchema().jsonify(treino)                
#             return make_response("Informações alteradas com sucesso", 200)

    def emailLiberacaoTreino(self, treino):
        try:
            msg = Message('Treino liberado.', recipients=[treino.usuario.email])
            msg.html = render_template('app/emailTreinoLiberado.html', enviado='Treinos', email='jullianoVolpato@gmail.com' , treino=treino) 
            mail.send(msg)
            return make_response("E-mail enviado com sucesso", 200)
        except Exception:
            pass
            return make_response("Erro no envio do e-mail", 500)
