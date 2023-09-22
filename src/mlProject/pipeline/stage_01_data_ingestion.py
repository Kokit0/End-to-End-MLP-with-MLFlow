from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger



STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline: #<-- El pipeline que diseñé en mi data_ingestion notebook
    def __init__(self):
        pass

    def main(self): #<-- El main method que llamaré desde main.py en carpeta raiz
        config = ConfigurationManager() #inicio mi ConfigurationManager
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file() #llamo el metodo de download
        data_ingestion.extract_zip_file()# llamo el metodo de extracción


    
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

