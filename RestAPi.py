from fastapi import FastAPI, HTTPException

app = FastAPI()

# Stateless/static data store (mock products catalog)
PRODUCTS = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999.99},
    {"id": 2, "name": "Coffee Mug", "category": "Kitchenware", "price": 14.99},
    {"id": 3, "name": "Headphones", "category": "Electronics", "price": 199.99},
    {"id": 13456, "name": "Headphones", "category": "Electronics", "price": 199.99}

]


# 1. GET Route: Health/Status Info
@app.get("/")
def get_status():
    return {
        "status": "Online",
        "message": "Stateless Data Server is running successfully."
    }

# 2. GET Route: List all products
@app.get("/products")
def get_products():
        return PRODUCTS

# 3. GET Route: Retrieve a specific product by ID
@app.get("/products/{product_id}")
def get_product(product_id: int):
    # Find product by ID
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    
    # Proper error handling: If not found, raise a 404 HTTP Exception
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
        
    return product

# 4. POST Route: Stateless Data Processing (Calculate discount and total)
@app.post("/calculate-total")
def calculate_total(data: dict):
    # Retrieve input data
    price = data.get("price", 0.0)
    quantity = data.get("quantity", 1)
    discount = data.get("discount", 0.0) # E.g., 0.1 for 10%

    # Basic business logic
    subtotal = price * quantity
    discount_amount = subtotal * discount
    total = subtotal - discount_amount

    # Return structured JSON response
    return {
        "subtotal": round(subtotal, 2),
        "discount_applied": round(discount_amount, 2),
        "total_price": round(total, 2)
    }

# for cretaing new products:
@app.post("/Create-products")
def create_product():
     a = {"id": 445, "name": "alice", "category": "Skincare", "price": 100000}
     PRODUCTS.append(a)
     return PRODUCTS
