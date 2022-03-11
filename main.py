import logging

from db.models import Users
from sanic import Sanic, response

from tortoise.contrib.sanic import register_tortoise

logging.basicConfig(level=logging.DEBUG)

app = Sanic(__name__)


@app.get("/user")
async def list_all(request):
    users = await Users.all()
    return response.json({"users": [str(user) for user in users]})


@app.post("/user")
async def add_user(request):
    user = await Users.create(**request.json)
    return response.json({"user": str(user)})


register_tortoise(
    app, db_url="mysql://root:sun890816@localhost/rust", modules={"models": ["db.models"]}, generate_schemas=True
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, debug=True)