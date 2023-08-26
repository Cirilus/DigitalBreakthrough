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
    __sort: int | None = None
    ksort: int | None = None
    time1: int | None = None
    time2: int | None = None
    dist: int | None = None
    id: int | None = None
    root: int | None = None
    kindId: int | None = None
    subjectId: int | None = None
    subjectParentId: int | None = None
    name: str | None = None
    brand: str | None = None
    brandId: int | None = None
    siteBrandId: int | None = None
    supplierId: int | None = None
    sale: int | None = None
    priceU: int | None = None
    salePriceU: int | None = None
    logisticsCost: int | None = None
    saleConditions: int | None = None
    returnCost: int | None = None
    pics: int | None = None
    rating: int | None = None
    reviewRating: int | None = None
    feedbacks: int | None = None
    volume: int | None = None
    colors: List[Color] | None = None
    sizes: List[Size] | None = None
    diffPrice: bool | None = None
