from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from model import Model
from conf import auth


model = Model(auth)
webserver = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8000",
]

webserver.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@webserver.get('/')
async def verif(request: Request):
    return 'Hello, World'

@webserver.get('/startups')
async def startups(request: Request):
    return model.get_startups()

@webserver.get('/startup')
async def startup(startup: int):
    data = model.get_startup(startup)
    if len(data):
        return data[0]
    return {}