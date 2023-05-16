from sanic import Sanic
from sanic.response import json
from jogos.bp import jogos_bp, ListarJogos

app = Sanic(__name__)
app.blueprint(jogos_bp)

jogos_bp.add_route(ListarJogos.as_view(), '/')

@app.route('/')
async def hello(request):
    return json({'message': 'Hello world!'})
