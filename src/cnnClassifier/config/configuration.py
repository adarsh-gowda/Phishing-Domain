from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import (DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
                                           )
"""from cnnClassifier.constants import * – Imports all constants, such as file paths or parameter names, 
        from a module named cnnClassifier.constants.
from cnnClassifier.utils.common import read_yaml, create_directories – 
        Imports helper functions to read YAML files (read_yaml) and to create directories (create_directories).
from cnnClassifier.entity.config_entity import DataIngestionConfig – Imports a configuration entity,
        DataIngestionConfig, which will hold the settings needed for data ingestion (like downloading or reading the dataset).
 """

class ConfigurationManager:
    """ConfigurationManager Class:
    This class is designed to read and manage configuration settings for various parts of the project, such as data ingestion."""


    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,              #cnnClassifier.constants
        params_filepath = PARAMS_FILE_PATH,              #cnnClassifier.constants
        schema_filepath = SCHEMA_FILE_PATH):             #ccnnClassifier.constants


        self.config = read_yaml(config_filepath)         #cnnClassifier.utils.common import read_yaml
        self.params = read_yaml(params_filepath)         #cnnClassifier.utils.common import read_yaml
        self.schema = read_yaml(schema_filepath)         #cnnClassifier.utils.common import read_yaml


        create_directories([self.config.artifacts_root])    #cnnClassifier.utils.common import create_directories


        """__init__ Method:

        Arguments:
        config_filepath, params_filepath, schema_filepath: Default to constants representing file paths (CONFIG_FILE_PATH, 
        PARAMS_FILE_PATH, and SCHEMA_FILE_PATH). These constants are likely defined in the cnnClassifier.constants module.
        Functionality:
        self.config = read_yaml(config_filepath) reads the configuration YAML file for the project settings, storing it in self.config.
        self.params = read_yaml(params_filepath) reads additional parameters, likely model parameters, storing it in self.params.
        self.schema = read_yaml(schema_filepath) reads a schema definition file, likely to validate the data, 
                    and stores it in self.schema.
        create_directories([self.config.artifacts_root]) creates a directory for storing artifacts (outputs, models, logs, etc.), 
                 using artifacts_root, which is expected to be defined in the configuration file."""


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:   #from cnnClassifier.entity.config_entity import (DataIngestionConfig,
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    """get_data_ingestion_config Method:

Purpose: This method retrieves and configures the settings for data ingestion.
Steps:
config = self.config.data_ingestion - Extracts the data ingestion configuration settings from self.config.
create_directories([config.root_dir]) - Ensures the root directory for data ingestion exists (e.g., a directory to store raw or processed data).
DataIngestionConfig Object:
Creates a DataIngestionConfig instance with the following settings:
root_dir: Root directory for data ingestion.
source_URL: URL for the source data.
local_data_file: Path for where the data file will be saved locally.
unzip_dir: Directory for unzipping the downloaded file (if needed).
Return: Returns an instance of DataIngestionConfig with the necessary parameters for data ingestion."""
    


    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    


    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config
    
    

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name
            
        )

        return model_trainer_config
    

    # def get_model_evaluation_config(self) -> ModelEvaluationConfig:
    #     config = self.config.model_evaluation
    #     params = self.params.ElasticNet
    #     schema =  self.schema.TARGET_COLUMN

    #     create_directories([config.root_dir])

    #     model_evaluation_config = ModelEvaluationConfig(
    #         root_dir=config.root_dir,
    #         test_data_path=config.test_data_path,
    #         model_path = config.model_path,
    #         all_params=params,
    #         metric_file_name = config.metric_file_name,
    #         target_column = schema.name
           
    #     )

    #     return model_evaluation_config