import base64
import http.client
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from starlette.middleware.cors import CORSMiddleware

from shemas import GeneratePresentation
from parsers import get_stat

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/v1/binary/generate")
async def generate_presentation_binary(request: GeneratePresentation):
    pdf = Path("test.pdf")
    return FileResponse(pdf, headers={"Content-Disposition": "attachment"})


@app.post("/api/v1/base64/generate")
async def generate_presentation_base64(request: GeneratePresentation):



    pdf = Path("test.pdf")
    with open(pdf, 'rb') as pdf_file:
        base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
    return JSONResponse(content={"pdf": base64_pdf})

@app.post("/api/v1/statistics")
async def get_statistics(request: GeneratePresentation):
    try:
        statistics = get_stat(request.product.field)
    except Exception as e:
        raise HTTPException(status_code=http.client.INTERNAL_SERVER_ERROR, detail="Item not found")

    return JSONResponse(content={"statistics": statistics})
