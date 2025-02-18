from pathlib import Path
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx

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
    
@main_router.get("/raw_storage", response_class=HTMLResponse)
async def raw_storage(request: Request):
    try:
        async with httpx.AsyncClient() as client:
            base_url = str(request.base_url)
            response = await client.get(f"{base_url}raw/get_all")
            if response.status_code == 200:
                data = response.json()
            else:
                raise HTTPException(status_code=response.status_code, detail="Failed to fetch data")    
        return templates.TemplateResponse("raw_storage.html", {"request": request, "data": data})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    
