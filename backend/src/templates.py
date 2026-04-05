from pathlib import Path
from fastapi.templating import Jinja2Templates

templates_path = Path(__file__).parent.parent / "frontend" / "templates"
templates = Jinja2Templates(directory=templates_path)