from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.data.company import COMPANY
from app.data.products import products

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/products")
def products_page(request: Request):

    return templates.TemplateResponse(
        name="products.html",
        request=request,
        context={
            "company": COMPANY,
            "products": products,
        },
    )