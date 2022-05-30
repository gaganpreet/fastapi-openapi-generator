from typing import List
from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    id: int
    name: str


items = [
    Item(id=1, name="Harry Potter"),
    Item(id=2, name="Lord of the Rings"),
    Item(id=3, name="The Hobbit"),
]


@app.get("/")
async def index():
    return {"hello": "world"}


@app.get("/items/", response_model=List[Item])
async def get_items():
    return items


@app.get("/items/{id}", response_model=Item)
async def get_item_by_id(id: int):
    return items[id]


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name


use_route_names_as_operation_ids(app)
