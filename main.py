from sensor.pipeline.training_pipeline import start_training_pipeline
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.pipeline.batch_prediction import start_batch_prediction


file_path="/config/workspace/aps_failure_training_set1.csv"
print(__name__) 
if __name__=="__main__":
     try:
          #start_training_pipeline()
          output_file = start_batch_prediction(input_file_path=file_path)
          print(output_file)
     except Exception as e:
          print(e)

 

 
       
          
   



"""from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys,os
 


if __name__ == "__main__":
     try:
          get_collection_as_dataframe(database_name="aps", collection_name="sensor")
     except Exception as e:
          print(e)   """