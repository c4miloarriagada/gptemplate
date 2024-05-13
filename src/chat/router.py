from chat.models import Message
from fastapi import APIRouter, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")


chat = APIRouter(prefix=r"/chat")


@chat.get("/")
async def chat_conversation_template(request: Request, response: HTMLResponse):
    name = "camilo"
    return templates.TemplateResponse("chat.html", {"request": request, name: name})


@chat.post("/")
async def chat_converstion(message: Message = Body()):
    return message
