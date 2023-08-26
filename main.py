from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
from shemas import GeneratePresentation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/v1/generate")
async def generate_presentation(request: GeneratePresentation):
    pdf = Path("test.pdf")
    return FileResponse(pdf, headers={"Content-Disposition": "attachment"})
