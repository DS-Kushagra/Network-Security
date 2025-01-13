import os
import sys
import json
import certifi

import pandas as pd
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')
ca = certifi.where()


class NetworkDataExtract:
    def __init__(self):
        pass

    def csv_to_json(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            logging.info(f"CSV data successfully loaded from: {file_path}")
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            logging.error("Error in csv_to_json")
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            mongo_client.admin.command('ping')  # Ping to verify connection
            logging.info("Successfully connected to MongoDB")

            db = mongo_client[database]
            col = db[collection]
            
            # Insert records in batches (if needed)
            BATCH_SIZE = 1000
            for i in range(0, len(records), BATCH_SIZE):
                col.insert_many(records[i:i + BATCH_SIZE])
                logging.info(f"Inserted batch {i // BATCH_SIZE + 1}")

            return f"Inserted {len(records)} records into {database}.{collection}"
        except pymongo.errors.ServerSelectionTimeoutError as timeout_error:
            logging.error("Server selection timeout. Check network access or credentials.")
            raise NetworkSecurityException(timeout_error, sys)
        except Exception as e:
            logging.error("Error during MongoDB insertion")
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    try:
        FILE_PATH = os.path.join("Network_Data", "phisingData.csv")
        DATABASE = "AISecurity"
        COLLECTION = "NetworkData"

        network_obj = NetworkDataExtract()
        records = network_obj.csv_to_json(file_path=FILE_PATH)
        logging.info(f"Total records to insert: {len(records)}")

        result = network_obj.insert_data_mongodb(records, DATABASE, COLLECTION)
        print(result)
    except Exception as e:
        logging.error("Error in main execution")
        raise NetworkSecurityException(e, sys)
