# Network Security Project

This project is a comprehensive solution for detecting and analyzing network security threats using machine learning techniques. The project automates data ingestion, validation, transformation, model training, and evaluation processes to detect phishing attacks. Below is the detailed overview of the project, its structure, and how to use it.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Modules Overview](#modules-overview)
7. [Configuration](#configuration)
8. [Model Evaluation](#model-evaluation)
9. [Logging and Exception Handling](#logging-and-exception-handling)
10. [Dataset Information](#dataset-information)
11. [Future Improvements](#future-improvements)

---

## Project Overview
The Network Security Project is designed to automate the detection of phishing websites. It leverages Python's ecosystem of machine learning and data processing libraries to train, validate, and test models capable of identifying phishing websites with high accuracy.

The project follows a modular design for:
- Data ingestion and preprocessing
- Model training and hyperparameter tuning
- Model evaluation
- YAML-based configuration for schema validation

---

## Features
- **Data Ingestion:** Reads and processes data from various sources.
- **Data Validation:** Validates datasets against a predefined schema.
- **Data Transformation:** Handles missing values, scaling, and encoding.
- **Model Training and Evaluation:** Includes hyperparameter tuning using GridSearchCV.
- **Exception Handling:** Provides robust error tracking and detailed logs.
- **YAML Configuration:** Makes the system highly configurable and reusable.
- **Logging:** Logs every operation with detailed timestamps for debugging and monitoring.

---

## Project Structure
```
NetworkSecurityProject/
├── training_pipeline/
│   ├── __init__.py
│   ├── constants.py
│   └── ...
├── networksecurity/
│   ├── exception/
│   │   └── exception.py
│   ├── logging/
│   │   └── logger.py
│   └── utils/
│       └── utils.py
├── data_schema/
│   └── schema.yaml
├── logs/
│   └── [Timestamped log files]
├── Artifacts/
│   ├── Data_Ingestion/
│   ├── Data_Validation/
│   ├── Data_Transformation/
│   └── Model_Trainer/
└── README.md
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/network-security.git
   cd network-security
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the `logs/` directory:
   ```bash
   mkdir logs
   ```

---

## Usage

1. **Edit Configuration:** Ensure the `schema.yaml` file matches your dataset schema.

2. **Run the Pipeline:** Execute the `training_pipeline` to ingest, validate, transform, and train the model:
   ```bash
   python main.py
   ```

3. **Logs:** Check logs for detailed execution details:
   ```bash
   tail -f logs/[latest-log-file.log]
   ```

---

## Modules Overview

### 1. Exception Handling
- **File:** `exception.py`
- **Purpose:** Captures and logs all exceptions with detailed traceback.
- **Key Methods:**
  - `__init__`: Parses exception details.
  - `__str__`: Returns a human-readable error message.

### 2. Logging
- **File:** `logger.py`
- **Purpose:** Configures and manages logging with timestamped files.
- **Features:** Logs to `logs/` directory with detailed format:
  ```
  [timestamp] line_number module_name - log_level - message
  ```

### 3. Utility Functions
- **File:** `utils.py`
- **Purpose:** Provides helper functions for YAML file operations, saving/loading models, and evaluating ML models.
- **Key Functions:**
  - `read_yaml_file`: Reads YAML configuration files.
  - `write_yaml_file`: Writes content to YAML files.
  - `save_object/load_object`: Saves and loads serialized objects.
  - `evaluate_models`: Trains and evaluates models using GridSearchCV.

### 4. Data Schema
- **File:** `schema.yaml`
- **Purpose:** Defines the schema for dataset validation, including column names and types.
- **Structure:**
  ```yaml
  columns:
    - column_name: data_type
  numerical_columns:
    - column_name
  ```

---

## Configuration
- **Target Column:** `Result`
- **Predefined Constants:**
  - Artifact directories for storing intermediate outputs.
  - Schema file for dataset validation.

---

## Model Evaluation

1. **GridSearchCV:**
   - Optimizes hyperparameters for each model.
   - Trains the model using the best parameters.

2. **Metrics:**
   - R-squared score (`r2_score`) to evaluate model accuracy.

3. **Outputs:**
   - Trained models saved in `Artifacts/Model_Trainer/`
   - Metrics logged for train and test datasets.

---

## Logging and Exception Handling

- **Log Files:** Automatically created in `logs/` directory with timestamps.
- **Exception Details:** Detailed traceback and error messages logged.

---

## Dataset Information
- **Input Features:**
  - `having_IP_Address`, `URL_Length`, `Shortining_Service`, ...
- **Target Column:**
  - `Result`
- **File Format:** CSV
- **Schema:**
  Defined in `schema.yaml`.

---

## Future Improvements
1. Add support for real-time data ingestion.
2. Implement additional ML algorithms.
3. Introduce deployment pipelines with Docker/Kubernetes.
4. Add feature engineering steps for better model accuracy.

---

Feel free to reach out with questions or suggestions! Happy coding!
