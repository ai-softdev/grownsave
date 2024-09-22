from fastapi import APIRouter
from sklearn.preprocessing import StandardScaler, LabelEncoder

from AImodels.dbo import ml_models, crop_model_loading
from schemas.crop import SCrop

import pandas as pd
import numpy as np

router = APIRouter(prefix="/area", tags=["Урожайность"])


@router.post("/")
async def root(data: SCrop):

    soil_info = data.soil_info.model_dump().items()
    soil_info = list(soil_info)
    numpyArray = np.array([[value for (feature, value) in soil_info]])
    data = pd.read_csv("AImodels/datasets/crop_data.csv")
    label_encoder = LabelEncoder()
    label_encoder.fit_transform(data["label"])
    data = ml_models["crop_prediction"].predict(np.array([numpyArray]).reshape(1, -1))
    predicted_class = label_encoder.inverse_transform([np.argmax(data)])

    return {"predicted_class": predicted_class[0]}
