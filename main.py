from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import json
import uvicorn
from types import SimpleNamespace


app = FastAPI()


@app.get("/get", response_class=HTMLResponse)
async def root(request: Request):
    return f"""</br>
    This is a {request.method} request</br></br>
    url: {request.url}</br></br>
    headers: {[f"{'</br>'+ str([word.decode('utf8') for word in sets])}" for sets in request.headers.raw]}</br></br>
    query_params: {request.query_params}</br></br>
    """


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port=8000)