import os
from sanic import Sanic
from jogos.bp import jogos_bp
from dotenv import load_dotenv
from tortoise.contrib.sanic import register_tortoise
from index.views import Index

load_dotenv()

app = Sanic(__name__)
app.blueprint(jogos_bp)

register_tortoise(
    app, db_url=os.getenv('CONNECTION_STRING'), modules={'models': ['jogos.models']}, generate_schemas=True
)

app.add_route(Index.as_view(), '/')
