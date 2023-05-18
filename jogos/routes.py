from jogos.views import ListarJogos, ListarJogo, BuscarJogo
from jogos.models import Jogos


def router(app):
    app.add_route(ListarJogos.as_view(), '/')
    app.add_route(ListarJogo.as_view(), '/<pk:int>')
    app.add_route(BuscarJogo.as_view(), '/buscar')
