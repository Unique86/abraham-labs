from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from app.routes.home import router as home_router

app = FastAPI()

from app.routes.home import router as home_router
from app.routes.about import router as about_router
from app.routes.products import router as products_router
from app.routes.cloud_file_automation import router as cloud_file_router
#from app.routes.contact import router as contact_router

app.include_router(home_router)
app.include_router(about_router)
app.include_router(products_router)
app.include_router(cloud_file_router)
#app.include_router(contact_router)


app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")



    