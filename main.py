from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataTransformationConfig,DataIngestionConfig, TrainingPipelineConfig,DataValidationConfig
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.entity.config_entity import ModelTrainerConfig
from networksecurity.components.model_tranier import ModelTrainer
import sys


if __name__ == '__main__':
    try:
        # Load training pipeline configuration
        trainingpipelineconfig = TrainingPipelineConfig()
        # Load data ingestion configuration
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate data ingestion configuration")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed")
        # Print data ingestion artifact
        logging.info(f"Data ingestion artifact: {dataingestionartifact}")
        print(dataingestionartifact)
        
        # Load data validation configuration
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)
        logging.info("Initiate data validation configuration")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        # Print data validation artifact
        logging.info(f"Data validation artifact: {data_validation_artifact}")
        
        # Load data transformation configuration
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        logging.info("Initiate data transfromation configuration")
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info("Data Tranformation Configuration completed")
        # Print data validation artifact
        logging.info(f"Data Transformation artifact: {data_transformation_artifact}")

        logging.info("Model Training Started...")
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("Model Training Artifact Created")
    except Exception as e:
        raise NetworkSecurityException(e,sys)