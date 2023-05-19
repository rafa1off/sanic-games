from jogos.views import ListarJogos, ListarJogo, BuscarJogo


def router(app):
    app.add_route(ListarJogos.as_view(), '/')
    app.add_route(ListarJogo.as_view(), '/<pk:int>')
    app.add_route(BuscarJogo.as_view(), '/buscar')
