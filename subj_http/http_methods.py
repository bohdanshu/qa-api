from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/methods", response_class=HTMLResponse, tags=["http methods"])
async def root(request: Request):
    return await req_info(request)


@router.post("/methods", response_class=HTMLResponse, tags=["http methods"])
async def root(request: Request):
    return await req_info(request)


@router.put("/methods", response_class=HTMLResponse, tags=["http methods"])
async def root(request: Request):
    return await req_info(request)


@router.delete("/methods", response_class=HTMLResponse, tags=["http methods"])
async def root(request: Request):
    return await req_info(request)


async def req_info(request):
    method_msg = f"</br> This is {request.method} reqest</br>"
    url_msg = f"</br> URL: {request.url}</br>"
    headers_list = [[word.decode('utf8') for word in sets] for sets in request.headers.raw]
    headers_msg = "</br>Headers:</br>"
    for list_ in headers_list:
        headers_msg += f"</br> {list_[0]} : {list_[1]}"
    query_msg = f"</br>Query_params: {request.query_params}</br>"

    try:
        json_data = await request.json()
    except BaseException as e:
        json_data = None
    return f"{method_msg} {url_msg} {query_msg} {headers_msg} </br> </br> {json_data if json_data else None}"


