from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Create FastAPI instance
app = FastAPI()

# Set up templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Home route
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Welcome to FastAPI Cloud Deployment!"})
