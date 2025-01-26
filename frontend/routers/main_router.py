from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

main_router = APIRouter(
    prefix='',
    tags=['frontend'],
)

templates = Jinja2Templates(directory="frontend/templates")

@main_router.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login_page.html", {"request": request})

@main_router.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
