from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline





STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")       #from cnnClassifier import logger
   data_ingestion = DataIngestionTrainingPipeline()               #from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)                                        #from cnnClassifier import logger
        raise e
