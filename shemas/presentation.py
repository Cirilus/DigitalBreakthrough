from pydantic import BaseModel


class GeneratePresentation(BaseModel):
    product: str | None = None
    country: str | None = None
