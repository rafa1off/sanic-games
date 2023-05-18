from sanic.views import HTTPMethodView
from sanic.response import json
from jogos.models import Jogos
from sanic.exceptions import NotFound

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
        jogo = await Jogos.get_or_none(pk=pk)
        if jogo is None:
            raise NotFound('Id not found')
        else:
            return json(dict(jogo))

    async def put(self, request, pk):
        jogo = await Jogos.get_or_none(pk=pk)
        if jogo is not None:
            await jogo.update_from_dict({
                'nome': request.json['nome'],
                'categoria': request.json['categoria'],
                'console': request.json['console']
            }).save()
            return json({'message': f'Jogo {jogo.nome} atualizado'})
        else:
            raise NotFound('Id not found')

    async def delete(self, request, pk):
        jogo = await Jogos.get(pk=pk)
        if jogo is not None:
            await jogo.delete()
            return json({'message': f'Jogo {jogo.nome} removido'})
        else:
            raise NotFound('Id not found')
