# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and document REST APIs using the FastAPI framework, including defining endpoints, handling requests, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description
Create a new FastAPI app that exposes REST endpoints for managing a simple product catalog.

#### Requirements
Completed application should:

- Use `FastAPI` to create the web application.
- Define at least three endpoints: `GET /products`, `GET /products/{product_id}`, and `POST /products`.
- Return JSON data for product responses.

### 🛠️ Add Request Validation and Response Models

#### Description
Add Pydantic models to validate incoming request data and define the shape of API responses.

#### Requirements
Completed application should:

- Define a `Product` model with fields: `id`, `name`, `price`, and `in_stock`.
- Validate `POST /products` request bodies using a Pydantic model.
- Return properly structured JSON using response models.

### 🛠️ Test Your API and Add Documentation

#### Description
Run the FastAPI app locally and verify the endpoints using the built-in interactive docs.

#### Requirements
Completed application should:

- Be able to start with `uvicorn starter_code:app --reload`.
- Use the automatically generated Swagger UI available at `/docs`.
- Demonstrate that `GET /products`, `GET /products/{product_id}`, and `POST /products` work as expected.
