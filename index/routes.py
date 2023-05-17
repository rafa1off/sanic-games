from index.views import Index

def router(app):
    app.add_route(Index.as_view(), '/')
