from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from airflow.sensors.filesystem import FileSensor

from constants import default_args, DEFAULT_VOLUME, DATASET_RAW_DIR,DATASET_TEMP_DIR, \
    MODELS_DIR, SCALER_NAME, MODEL_NAME, SCORES_NAME, DATASET_SPLITTED_DIR, DATASET_PREPROCESSED_DIR


with DAG(
    "1_train",
    default_args=default_args,
    description="DAG to preprocess data and train model",
    schedule_interval="@weekly",
    start_date=days_ago(2),
) as dag:

    start = DummyOperator(
        task_id="Start_the_pipeline"
    )

    check_model = FileSensor(
        task_id="Check_model_exist",
        poke_interval=10,
        retries=100,
        filepath="data/models/{{ ds }}/model.pkl"
    )

    check_metrics = FileSensor(
        task_id="Check_metrics_exist",
        poke_interval=10,
        retries=100,
        filepath="data/models/{{ ds }}/scores.json"
    )

    load = DockerOperator(
        task_id="Download_data",
        image="airflow-load",
        command=f"--input-path {DATASET_RAW_DIR} --temp-path {DATASET_TEMP_DIR}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[DEFAULT_VOLUME]
    )

    preprocess = DockerOperator(
        task_id="Preprocess_features",
        image="airflow-preprocess",
        command=f"--temp-path {DATASET_TEMP_DIR} --preprocessed-path {DATASET_PREPROCESSED_DIR} --scaler-path {MODELS_DIR}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[DEFAULT_VOLUME]
    )

    split = DockerOperator(
        task_id="Split_data",
        image="airflow-split",
        command=f"--preprocessed-path {DATASET_PREPROCESSED_DIR} --splitted-path {DATASET_SPLITTED_DIR}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[DEFAULT_VOLUME]
    )

    train = DockerOperator(
        task_id="Train_model",
        image="airflow-train",
        command=f"--train-path {DATASET_SPLITTED_DIR} --model-path {MODELS_DIR}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[DEFAULT_VOLUME]
    )

    validate = DockerOperator(
        task_id="Validate_model",
        image="airflow-validate",
        command=f"--val-path {DATASET_SPLITTED_DIR} --metrics-path {MODELS_DIR} --model-path {MODELS_DIR}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[DEFAULT_VOLUME]
    )

    finish = DummyOperator(
        task_id="Finish_pipeline"
    )

    start >> load >> preprocess >> split >> train >> validate >> [check_model, check_metrics] >> finish
