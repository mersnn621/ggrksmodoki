from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/{path:path}")
async def catch_all(path: str, request: Request):
    new_path = f'https://www.google.com/search?q={path}'
    response = templates.TemplateResponse("hoge.html",status_code=302,context={"request": request})
    return response

if __name__ == "__main__":
    uvicorn.run(app,port=80)