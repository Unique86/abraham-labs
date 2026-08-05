from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.data.company import COMPANY

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/products/cloud-file-automation")
def cloud_file_automation(request: Request):

    return templates.TemplateResponse(
        name="cloud_file_automation.html",
        request=request,
        context={
            "company": COMPANY,
        },
    )