from textSummarizer.config.configuration import Configuration
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger


class DataIngesionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configuration()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
