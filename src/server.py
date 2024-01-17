import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse

from src.routes.sprites_lpc import router as SpriteLPCRouter

load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT")

# CORS
origins = [
    'http://localhost',
    'https://universal-lpc-spritesheet-character-generator.vercel.app'
    ]



description = """
Ola meus queridos, criamos essa API para melhor nossos sprites. 🚀


* **API LPC Sprites** (_EM PROGRESSO_).
"""

app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Jogatinando API - LPC Sprites",
        description=description,
        version="0.0.1",
        terms_of_service="https://jogatinando.com.br/#terms",
        routes=app.routes,
        contact={
        "name": "Sulivan T. Leite",
        "url": "https://jogatinando.com/#contact",
        "email": "contato@jogatinando.com",
    },    
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(SpriteLPCRouter, tags=["LPC Sprites"], prefix="/lpc")
    