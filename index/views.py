from sanic.response import json
from sanic.views import HTTPMethodView

class Index(HTTPMethodView):
    async def get(self, request):
        return json({'message': 'Hello world!'})
