import os
from sanic import Sanic
from jogos.bp import jogos_bp
from tortoise.contrib.sanic import register_tortoise
from index.routes import router

app = Sanic(__name__)
app.blueprint(jogos_bp)

register_tortoise(
    app,
    db_url=os.getenv('CONNECTION_STRING'),
    modules={'models': ['jogos.models']},
    generate_schemas=True
)

router(app)
