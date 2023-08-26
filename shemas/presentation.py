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


class GeneratePresentation(BaseModel):
    product_idea: str
    team: List[TeamMember]
    market: str
    roadmap: str
    economy: Economy
