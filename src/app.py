from functools import lru_cache
import os
import pathlib
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from .airtable import push, get
from .tasks import parse_and_publish

BASE_DIR = pathlib.Path(__file__).parent

app = FastAPI()
templates = Jinja2Templates(directory= BASE_DIR/ "templates")

@app.get("/")
async def home_view(request: Request):
    list_of_quotes = get()
    return templates.TemplateResponse("base.html", {
        "request": request,
        "list_of_quotes": list_of_quotes[-10:],
    })