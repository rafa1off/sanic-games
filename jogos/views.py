from sanic.views import HTTPMethodView
from sanic.response import json
from jogos.models import Jogos
from sanic.exceptions import NotFound


class ListarJogos(HTTPMethodView):
    async def get(self, request):
        if request.args.get('limite') and request.args.get('pagina'):
            limite = int(request.args.get('limite'))
            pagina = int(request.args.get('pagina')) - 1
            jogos = await Jogos.all().limit(limite).offset(pagina).values()
            return json([jogo for jogo in jogos])
        elif request.args.get('limite'):
            limite = int(request.args.get('limite'))
            jogos = await Jogos.all().limit(limite).values()
            return json([jogo for jogo in jogos])

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


class BuscarJogo(HTTPMethodView):
    async def get(self, request):
        if request.args.get('nome'):
            jogos = await Jogos.filter(nome__icontains=request.args.get('nome')).values()
            return json([jogo for jogo in jogos])
        elif request.args.get('categoria'):
            jogos = await Jogos.filter(categoria__icontains=request.args.get('categoria')).values()
            return json([jogo for jogo in jogos])
        elif request.args.get('console'):
            jogos = await Jogos.filter(console__icontains=request.args.get('console')).values()
            return json([jogo for jogo in jogos])
