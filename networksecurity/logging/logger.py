import logging
import os
from datetime import datetime

# Define the log file name with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.log"

# Define the path for the logs directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the logs directory if it doesn't exist
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# Define the full log file path
LOG_FILE_PATH = logs_path

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
