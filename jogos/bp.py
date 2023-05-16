from sanic import Blueprint, text
from sanic.views import HTTPMethodView
from sanic.response import json
from db import db

jogos_bp = Blueprint('jogos', url_prefix='/jogos')


class ListarJogos(HTTPMethodView):
    async def get(self, request):
        lista_jogos = []
        for jogo in db.jogos.find():
            lista_jogos.append({
                'nome': jogo['nome'],
                'categoria': jogo['categoria'],
                'console': jogo['console']
            })
        return json(lista_jogos)

    async def post(self, request):
        db.jogos.insert_one(request.json)
        return json({'message': 'Jogo ' + request.json['nome'] + ' adicionado'})
