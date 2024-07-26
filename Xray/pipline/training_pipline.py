import sys
from Xray.components.data_ingestion import DataIngestion
from Xray.components.data_transformation import DataTransformation
from Xray.components.model_training import ModelTrainer
from Xray.components.model_evaluation import ModelEvaluation
from Xray.components.model_pusher import ModelPusher
from Xray.entity.config_entity import DataIngestionConfig
from Xray.exception import XRayException
from Xray.logger import logging

class TrainPipline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
     
    def start_data_ingestion(self) -> DataIngestionArtifacts()
        self