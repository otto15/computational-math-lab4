from fastapi import FastAPI
from dto.response import ApproxResultTo
from dto.request import ApproxRequestTo
from approximation.approximation_manager import approximate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/approximation")
async def approx(approximation_data: ApproxRequestTo) -> ApproxResultTo:
    return approximate(approximation_data)
