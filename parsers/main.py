import json
from typing import List
from .models import Product
import requests


def get_url(product_field):
    url = (f"https://search.wb.ru/exactmatch/ru/common/v4/"
           "search?TestGroup=no_test&TestID=no_test&appType=1"
           f"&curr=rub&dest=-1257786&query={product_field}&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,1,31,66,22,110,48,71,114"
           f"&resultset=catalog&sort=popular&spp=0&suppressSpellcheck=false")
    return url


def get_headers():
    return {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Origin': 'https://www.wildberries.by',
        'Referer': 'https://www.wildberries.by/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'sec-ch-ua': 'Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'macOS',
    }




def get_products(headers, url):
    req = requests.get(url=url, headers=headers)
    if req.status_code != 200:
        raise Exception("Bad req")

    req = req.text

    req = json.loads(req)
    req_products = req["data"]["products"]

    products = []

    for req_product in req_products:
        product = Product()
        product.__sort = req_product.get("__sort", None)
        product.ksort = req_product.get("ksort", None)
        product.time1 = req_product.get("time1", None)
        product.time2 = req_product.get("time2", None)
        product.dist = req_product.get("dist", None)
        product.id = req_product.get("id", None)
        product.root = req_product.get("root", None)
        product.kindId = req_product.get("kindId", None)
        product.subjectId = req_product.get("subjectId", None)
        product.subjectParentId = req_product.get("subjectParentId", None)
        product.name = req_product.get("name", None)
        product.brand = req_product.get("brand", None)
        product.brandId = req_product.get("brandId", None)
        product.siteBrandId = req_product.get("siteBrandId", None)
        product.supplierId = req_product.get("supplierId", None)
        product.sale = req_product.get("sale", None)
        product.priceU = req_product.get("priceU", None)
        product.salePriceU = req_product.get("salePriceU", None)
        product.logisticsCost = req_product.get("logisticsCost", None)
        product.saleConditions = req_product.get("saleConditions", None)
        product.returnCost = req_product.get("returnCost", None)
        product.pics = req_product.get("pics", None)
        product.rating = req_product.get("rating", None)
        product.reviewRating = req_product.get("reviewRating", None)
        product.feedbacks = req_product.get("feedbacks", None)
        product.volume = req_product.get("volume", None)
        product.colors = req_product.get("colors", None)
        product.sizes = req_product.get("sizes", None)
        product.diffPrice = req_product.get("diffPrice", None)

        products.append(product)

    return products


def get_stat(product_field):
    headers = get_headers()
    url = get_url(product_field)
    products = get_products(headers, url)

    stat = {}
    sum_price = 0
    for product in products:
        sum_price += product.salePriceU / 100
    stat["average_price"] = sum_price / len(products)
    stat["min_price"] = min([i.salePriceU for i in products]) / 100
    stat["max_price"] = max([i.salePriceU for i in products]) / 100
    stat["count"] = len(products)

    return stat


if __name__ == '__main__':
    get_stat("носки")


