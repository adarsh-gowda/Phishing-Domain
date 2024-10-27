from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_data_validation import DataValidationTrainingPipeline




STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")       #from cnnClassifier import logger
   data_ingestion = DataIngestionTrainingPipeline()               #from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)                                        #from cnnClassifier import logger
        raise e


STAGE_NAME = "Data Validation stage"

try:
    config = ConfigurationManager()
    data_validation_config = config.get_data_validation_config()
    data_validation = DataValiadtion(config=data_validation_config)
    data_validation.validate_all_columns()
except Exception as e:
    raise e