from fastapi import FastAPI

from app.api import healthcheck

app = FastAPI()

app.include_router(healthcheck.router)


# @app.get("/healthcheck")
# async def healthcheck():
#     return {"healthcheck": "ok"}


# @app.get("/notes")
# async def get_notes():
#     return {"notes": "notes"}


# @app.get("/notes/{id}")
# async def get_note():
#     return {"note": "note"}


# @app.post("/notes")
# async def post_note():
#     return {"note": "note"}


# @app.put("/notes/{id}")
# async def put_note():
#     return {"note": "note"}


# @app.delete("/notes/{id}")
# async def delete_note():
#     return {"note": "note"}
