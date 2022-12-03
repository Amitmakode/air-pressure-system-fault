import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

Datafile_path = "/config/workspace/aps_failure_training_set1.csv"
Database_name = "aps"
Collection_name = "sensor"


if __name__ == "__main__":
    df = pd.read_csv(Datafile_path)
    print(f"Rows and Columns: {df.shape} ")

    #convert data frame into json formate for dump data in mongoDB
    df.reset_index(drop = True, inplace = True )

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record [0])

    #insert converted record to mongoDB
    client[Database_name][Collection_name].insert_many(json_record)

    


