from dataclasses import dataclass
from typing import List


@dataclass
class Color:
    name: str
    id: int


class Size:
    name: str
    origName: str
    rank: int
    optionId: int
    returnCost: int
    wh: int
    sign: str


@dataclass(init=False)
class Product:
    __sort: int = 0
    ksort: int = 0
    time1: int = 0
    time2: int = 0
    dist: int = 0
    id: int = 0
    root: int = 0
    kindId: int = 0
    subjectId: int = 0
    subjectParentId: int = 0
    name: str | None = None
    brand: str | None = None
    brandId: int = 0
    siteBrandId: int = 0
    supplierId: int = 0
    sale: int = 0
    priceU: int = 0
    salePriceU: int = 0
    logisticsCost: int = 0
    saleConditions: int = 0
    returnCost: int = 0
    pics: int = 0
    rating: int = 0
    reviewRating: int = 0
    feedbacks: int = 0
    volume: int = 0
    colors: List[Color] | None = None
    sizes: List[Size] | None = None
    diffPrice: bool | None = None
