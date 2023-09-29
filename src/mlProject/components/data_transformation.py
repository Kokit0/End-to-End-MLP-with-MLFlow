import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    
    ## Note: Aquí podemos agregar diferentes tecnicas de tranformacion de data  como Scaler, PCA y todo eso.
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up


    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False) #<--- mandara a la ruta para almacenar el train.csv en el data transformation folder
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False) #<--- mandara a la ruta para almacenar el test.csv en el data transformation folder

        logger.info("Splited data into training and test sets") #<--- logeamos el proceso en terminal y en el log
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)

        