print("home.py imported")
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.data.company import COMPANY, MISSION
from app.routes.products import products
from app.data.services import services


router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(name="home.html", 
                                      request=request, 
                                      context={"company": COMPANY,
                                               "products": products,
                                               "services": services,
                                               "mission": MISSION}) 