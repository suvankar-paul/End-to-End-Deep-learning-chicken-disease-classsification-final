from src.cnnClassifier import logger  # Adjusted the import path to include the 'src' directory
from src.cnnClassifier.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.model_trainer import ModelTrainingPipeline
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Training the model"
try:  
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   from src.cnnClassifier.pipeline.model_trainer import ModelTrainingPipeline
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e
