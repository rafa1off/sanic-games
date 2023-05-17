from sanic import Blueprint
from jogos.views import ListarJogos, ListarJogo

jogos_bp = Blueprint('jogos', url_prefix='/jogos')

jogos_bp.add_route(ListarJogos.as_view(), '/')
jogos_bp.add_route(ListarJogo.as_view(), '/<pk:int>')
