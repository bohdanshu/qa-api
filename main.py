from fastapi import FastAPI, Request
from subj_http import http_methods, http_statuses
from subj_qa_techniques import equity_classes, boundary_values
app = FastAPI()

tags_metadata = [
    {
        "name": "equity classes",
        "description": "Some examples for mastering qa techniques",
    },
    {
        "name": "boundary values",
        "description": "Some examples for mastering qa techniques",
    },
    {
        "name": "http methods",
        "description": "HTTP methods examples",
    },
    {
        "name": "http statuses",
        "description": "HTTP statuses examples",
    },
]


app.include_router(http_methods.router)
app.include_router(equity_classes.router)
app.include_router(boundary_values.router)
app.include_router(http_statuses.router)
