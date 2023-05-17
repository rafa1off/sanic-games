from sanic import Blueprint
from sanic.views import HTTPMethodView
from sanic.response import json
from jogos.models import Jogos

jogos_bp = Blueprint('jogos', url_prefix='/jogos')


class ListarJogos(HTTPMethodView):
    async def get(self, request):
        return json([dict(jogo) for jogo in await Jogos.all()])

    async def post(self, request):
        await Jogos(nome=request.json['nome'],
                    categoria=request.json['categoria'],
                    console=request.json['console']).save()
        return json({'message': 'Jogo adicionado'})


class ListarJogo(HTTPMethodView):
    async def get(self, request, pk):
        return json(dict(await Jogos.get(pk=pk)))

    async def put(self, request, pk):
        jogo = await Jogos.get(pk=pk)
        await jogo.update_from_dict({
            'nome': request.json['nome'],
            'categoria': request.json['categoria'],
            'console': request.json['console']
        }).save()
        return json({'message': f'Jogo {jogo.nome} atualizado'})

    async def delete(self, request, pk):
        jogo = await Jogos.get(pk=pk)
        await jogo.delete()
        return json({'message': f'Jogo {jogo.nome} removido'})
