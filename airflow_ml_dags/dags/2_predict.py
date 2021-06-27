from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from airflow.sensors.filesystem import FileSensor

from constants import default_args, DEFAULT_VOLUME, DATASET_RAW_DIR, DATASET_PREDS_DIR, MODELS_DIR

with DAG(
        '2_prediction',
        default_args=default_args,
        description='A DAG to make a prediction',
        schedule_interval="@daily",
        start_date=days_ago(2),
) as dag:
    start = DummyOperator(
        task_id='Start_predicting'
    )

    check_model = FileSensor(
        task_id="Check_model_creation",
        poke_interval=10,
        retries=100,
        filepath="data/models/{{ ds }}/model.pkl"
    )

    check_prediction = FileSensor(
        task_id="Check_predictions_exists",
        poke_interval=10,
        retries=100,
        filepath="data/predictions/{{ ds }}/predictions.csv"
    )

    predict = DockerOperator(
        task_id='Make_prediction',
        image='airflow-predict',
        command=f'--input-path {DATASET_RAW_DIR} --prediction-path {DATASET_PREDS_DIR} '
                f'--scaler-path {MODELS_DIR} --model-path {MODELS_DIR}',
        network_mode="bridge",
        do_xcom_push=False,
        volumes=[DEFAULT_VOLUME]
    )

    finish = DummyOperator(
        task_id="Finish_prediction"
    )

    start >> check_model >> predict >> check_prediction >> finish
