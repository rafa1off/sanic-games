import os
from sanic import Sanic
from jogos.bp import jogos_bp
from tortoise.contrib.sanic import register_tortoise
from index.routes import router
from dotenv import load_dotenv

load_dotenv()

app = Sanic(__name__)
app.blueprint(jogos_bp)

app.config.FALLBACK_ERROR_FORMAT = 'json'

register_tortoise(
    app,
    db_url=os.getenv('CONNECTION_STRING'),
    modules={'models': ['jogos.models']},
    generate_schemas=True
)

router(app)
