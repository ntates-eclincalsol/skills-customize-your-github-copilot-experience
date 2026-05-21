from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

class ProductCreate(BaseModel):
    name: str
    price: float
    in_stock: bool

products: List[Product] = [
    Product(id=1, name="Wireless Mouse", price=25.99, in_stock=True),
    Product(id=2, name="Mechanical Keyboard", price=79.99, in_stock=True),
    Product(id=3, name="USB-C Hub", price=39.95, in_stock=False),
]

@app.get("/products", response_model=List[Product])
def list_products():
    return products

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products", response_model=Product, status_code=201)
def create_product(product: ProductCreate):
    next_id = max([p.id for p in products], default=0) + 1
    new_product = Product(id=next_id, **product.dict())
    products.append(new_product)
    return new_product
