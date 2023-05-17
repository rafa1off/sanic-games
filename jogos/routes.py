from jogos.views import ListarJogos, ListarJogo

def router(app):
    app.add_route(ListarJogos.as_view(), '/')
    app.add_route(ListarJogo.as_view(), '/<pk:int>')
