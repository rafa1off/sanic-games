from sanic import Blueprint
from jogos.routes import router

jogos_bp = Blueprint('jogos', url_prefix='/jogos')

router(jogos_bp)
