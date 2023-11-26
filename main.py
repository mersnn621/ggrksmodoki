from fastapi import FastAPI
from fastapi.responses import RedirectResponse


app = FastAPI()

@app.get("/{path:path}")
async def catch_all(path: str):
    new_path = f'https://www.google.com/search?q={path}'
    response = RedirectResponse(url=new_path, status_code=302)
    return response