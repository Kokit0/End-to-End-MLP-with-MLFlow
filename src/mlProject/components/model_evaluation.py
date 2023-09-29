import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from mlProject.entity.config_entity import ModelEvaluationConfig #agregamos la config del model evaluation.
from mlProject.utils.common import save_json # importamos tambien el save json
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    
    def eval_metrics(self,actual, pred): #<--- definimos las Evaluation Metrics aquí. rmse, r2, MAE, etc.
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    


    def log_into_mlflow(self): # creamos el df test_data en base al dataset, cargamos el modelo, y generamos el split train/test, usando Dropeo del objetivo

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]


        mlflow.set_registry_uri(self.config.mlflow_uri) # seteo mi tracker URI para que todo ocurra en mi servidor remoto
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        with mlflow.start_run():

            predicted_qualities = model.predict(test_x) #<--- predicted value

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities) #<--- calcula las 3 metricas
            
            # Salvamos metrics en el .json local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae) # así va guardando todos los parámetros en MLflow

            # Con esto verificamos que vaya guardando todo en el URI o en el local drive.
            # (Model registry does not work with file store)
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel") #<--- por ultimo le damos el modelo que queremos (ElasticNet).
            else:
                mlflow.sklearn.log_model(model, "model")