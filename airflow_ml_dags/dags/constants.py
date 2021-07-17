from datetime import timedelta

DEFAULT_VOLUME = 'C:/Users/User/PycharmProjects/airflow_ml_dags/data:/data'

default_args = {
    'owner': "airflow",
    'depends_on_past': False,
    'email': ["troubleshooting@example.com"],
    'email_on_failure': True,
    'email_on_retry': True,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

DATASET_RAW_DIR = "/data/raw/{{ ds }}"
DATASET_TEMP_DIR = "/data/temp_dir/{{ ds }}"
MODELS_DIR = "/data/models/{{ ds }}"
DATASET_PREPROCESSED_DIR = "/data/preprocessed/{{ ds }}"
DATASET_SPLITTED_DIR = "/data/splitted/{{ ds }}"
DATASET_PREDS_DIR = "/data/predictions/{{ ds }}"


SCALER_NAME = "scaler.pkl"
MODEL_NAME = "model.pkl"
SCORES_NAME = "scores.json"