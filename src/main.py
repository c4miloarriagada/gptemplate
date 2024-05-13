import uvicorn
from chat.router import chat
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(chat)

templates = Jinja2Templates(directory="templates")


load_dotenv()


@app.get(r"/")
async def home(request: Request, response: HTMLResponse):
    return templates.TemplateResponse("home.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="127.0.0.1", port=8000, reload=True, reload_includes="*.html"
    )
