from keras.src.saving import load_model
from pathlib import Path

print(Path("saved/crop.h5"))

ml_models = {}


def crop_model_loading():
    model = load_model("AImodels/saved/crop.h5")
    print(model.summary())

    return model
