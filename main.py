from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/method", response_class=HTMLResponse)
async def root(request: Request):
    method_msg = f"</br> This is {request.method} reqest</br>"
    url_msg = f"</br> URL: {request.url}</br>"
    headers_msg = stringify_headers(request.headers.raw)
    query_msg = f"</br>Query_params: {request.query_params}</br>"
    return f"{method_msg} {url_msg} {query_msg} {headers_msg}"


@app.post("/method", response_class=HTMLResponse)
async def root(request: Request):
    method_msg = f"</br> This is {request.method} reqest</br>"
    url_msg = f"</br> URL: {request.url}</br>"
    headers_msg = stringify_headers(request.headers.raw)
    query_msg = f"</br>Query_params: {request.query_params}</br>"
    try:
        jsondata = await request.json()
    except Exception as e:
        print(e)
        jsondata = None
    return f"{method_msg} {url_msg} {query_msg} {headers_msg} </br> </br> {jsondata if jsondata else None}"


@app.put("/method", response_class=HTMLResponse)
async def root(request: Request):
    method_msg = f"</br> This is {request.method} reqest</br>"
    url_msg = f"</br> URL: {request.url}</br>"
    headers_msg = stringify_headers(request.headers.raw)
    query_msg = f"</br>Query_params: {request.query_params}</br>"
    try:
        jsondata = await request.json()
    except Exception as e:
        print(e)
        jsondata = None
    return f"{method_msg} {url_msg} {query_msg} {headers_msg} </br> </br> {jsondata if jsondata else None}"


@app.delete("/method", response_class=HTMLResponse)
async def root(request: Request):
    method_msg = f"</br> This is {request.method} reqest</br>"
    url_msg = f"</br> URL: {request.url}</br>"
    headers_msg = stringify_headers(request.headers.raw)
    query_msg = f"</br>Query_params: {request.query_params}</br>"
    try:
        jsondata = await request.json()
    except Exception as e:
        print(e)
        jsondata = None
    return f"{method_msg} {url_msg} {query_msg} {headers_msg} </br> </br> {jsondata if jsondata else None}"

def stringify_headers(headers):
    headers_list = [[word.decode('utf8') for word in sets] for sets in headers]
    html_headers = "</br>Headers:</br>"
    for list_ in headers_list:
        html_headers += f"</br> {list_[0]} : {list_[1]}"
    return html_headers
