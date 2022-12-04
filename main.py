from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys,os
from sensor.entity import config_entity
from sensor.components.data_ingestion import DataIngestion

def test_logger_and_exception():
     try:
          result = 3/0
          print (result)
          pass
     except Exception as e:
          raise SensorException(e, sys)


if __name__ == "__main__":
     try:
          pass
     except Exception as e:
          print(e)