import azure.functions as func
from fastapi import FastAPI, Request, Response
import logging

fast_app = FastAPI()

@fast_app.exception_handler(Exception)
async def handle_exception(request: Request, exc: Exception):
    return Response(
        status_code=400,
        content={"message": str(exc)},
    )

@fast_app.get("/")
async def home():
    return {
        "info": "Try the API path for success" 
    }

@fast_app.get("/v1/test/{test}")
async def get_test(
    test: str,):
    return {
        "test": test,
    }

app = func.AsgiFunctionApp(app=fast_app,
                           http_auth_level=func.AuthLevel.ANONYMOUS,)
