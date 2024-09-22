from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from AImodels.dbo import crop_model_loading, ml_models
from endpoints.crop import router as crop_router


@asynccontextmanager
async def lifespan():
    ml_models["crop_prediction"] = crop_model_loading()
    yield
    ml_models.clear()


app = FastAPI(lifespan=lifespan, docs_url=None, redoc_url=None)
app.include_router(crop_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
