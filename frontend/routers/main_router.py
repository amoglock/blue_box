from pathlib import Path
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.templates import templates


main_router = APIRouter(
    prefix='',
    tags=['frontend'],
)

@main_router.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    try:
        return templates.TemplateResponse("login_page.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@main_router.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    try:
        return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
