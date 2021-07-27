from typing import Optional

from fastapi import FastAPI

app = FastAPI()


# basic method
@app.get("/")
def read_root():
    return {"Hello": "World"}

# path parameter
# if item_id got other type except int, it show type error (data validation check)
# 127.0.0.1:8000/items/3
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return { "item_id" : item_id }


# query parameter
# if skip, limit got other type except int, it show type error (data validation check)
# 127.0.0.1:8000/items/?skip=0&limit=0
# if don't input value of skip and limit, it get fixed value 0 (cuz int=0)
# but like 127.0.0.1:8000/items/?skip=10&limit=100, if they get other values, results are same with other values.
# so int=0 <= it is default of query
@app.get("/items/")
def read_item_query(skip: int=0, limit: int=0):
    return {"skip":skip, "limit":limit}
# and get url query => q: ~~
# 127.0.0.1:8000/items/3?q=hello => return {"item_id":3, "q": "hello" }

# query Optional
# q is just option, so don't input any query, its default is None.
# item_id = url parameter , def_q = query, op_q = optional query
# when I make path /items/3?def_q="hello"&op_q="hello2", function read_item's path is simiral with it
# so can't redirect function read_item_params, modify path items => item
@app.get("/item/{item_id}")
def read_item_params(item_id: int, def_q: str='hello', op_q: Optional[str] = None):
    return {"item_id": item_id, "def_q": def_q, "op_q": op_q}

# Body?!

@app.post("/items")
def create_item():
    return