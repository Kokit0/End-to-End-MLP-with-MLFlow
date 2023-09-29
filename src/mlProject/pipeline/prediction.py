import joblib 
import numpy as np
import pandas as pd
from pathlib import Path



class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib')) # cargamos el modelo y le damos el path

    
    def predict(self, data): # detectara el data del usuario lo predice y lo devuelve.
        prediction = self.model.predict(data)

        return prediction