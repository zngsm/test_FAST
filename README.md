# README

CRUD API server using FAST API

[Fast API reference](https://fastapi.tiangolo.com/ko/)



## Getting start

- python 3.6+ (IDE pycharm)

- in virtual environment

```sh
$ pip install fastapi
$ pip install uvicorn[standard]
```

- fastapi
  - framework
- uvicorn[standard]
  - ASGI server



- run server

```sh
$ uvicorn main:app --reload
```

> http://127.0.0.1:8000





## Docs

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/redoc

if you run, fast api make swagger and redoc automatically. 





## CRUD

create `main.py`

```python
from typing import Optional

from fastapi import FastAPI

app = FastAPI()
```



- make restAPI

> make url `@app.[api method]("resource")`



- read

```python
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
```

