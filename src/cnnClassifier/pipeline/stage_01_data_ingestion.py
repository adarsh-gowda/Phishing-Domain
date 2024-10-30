from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()                                      #from cnnClassifier.config.configuration import ConfigurationManager
        data_ingestion_config = config.get_data_ingestion_config()           #from cnnClassifier.config.configuration import ConfigurationManager
        data_ingestion = DataIngestion(config=data_ingestion_config)         #from cnnClassifier.config.configuration import ConfigurationManager
        data_ingestion.download_file()
        data_ingestion.save_to_unzip_path()

        