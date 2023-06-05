from fastapi import FastAPI, Request
from subj_http import http_methods, http_statuses
from subj_qa_techniques import equity_classes
app = FastAPI()

tags_metadata = [
    {
        "name": "qa techniques",
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
app.include_router(http_statuses.router)
