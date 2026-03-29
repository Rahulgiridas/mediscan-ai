from fastapi import FastAPI
from app.routes.upload import router as upload_router

app = FastAPI(title="MediScan AI")

app.include_router(upload_router)

@app.get("/")
def root():
    return {"message": "MediScan AI Backend Running 🚀"}
