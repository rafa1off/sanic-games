from sanic import Sanic
from sanic.response import json
from jogos.bp import jogos_bp, ListarJogos, ListarJogo
import os
from dotenv import load_dotenv
from tortoise.contrib.sanic import register_tortoise

load_dotenv()

app = Sanic(__name__)
app.blueprint(jogos_bp)

register_tortoise(
    app, db_url=os.getenv('CONNECTION_STRING'), modules={'models': ['jogos.models']}, generate_schemas=True
)

jogos_bp.add_route(ListarJogos.as_view(), '/')
jogos_bp.add_route(ListarJogo.as_view(), '/<pk:int>')

@app.route('/')
async def hello(request):
    return json({'message': 'Hello world!'})
