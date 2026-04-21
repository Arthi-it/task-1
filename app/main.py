from fastapi import FastAPI
from app.routers import search   # ✅ FIXED
from app.services.indexer import Indexer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

indexer = Indexer("documents")
indexer.build_index()

search.indexer = indexer

app.include_router(search.router)