from typing import List
from pydantic import BaseModel


class TeamMember(BaseModel):
    name: str
    role: str


class Economy(BaseModel):
    revenue: float
    number_of_clients: float
    APRU: int
    churn_rate: int
    LT: int
    LTV: int


class Product(BaseModel):
    product_idea: str
    market: str
    roadmap: str


class GeneratePresentation(BaseModel):
    product: Product
    team: List[TeamMember]
    economy: Economy
