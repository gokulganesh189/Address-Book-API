from fastapi import FastAPI, Response
from .database import Base, engine
from .routers import address
from .logging_config import setup_logging

setup_logging()

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")

app.include_router(address.router)

@app.get('/')
def healthcheck(response = Response):
    response.status_code = 200
    return {"status": "Address Book Api is working fine"}
