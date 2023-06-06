from textSummarizer.pipeline.stage_01_data_ingestion import DataIngesionTrainingPipeline

from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngesionTrainingPipeline()
    data_ingestion.main()
    logger.info(
        f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx================================x")

except Exception as e:
    logger.exception((e))
    raise e
