from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.sensors import ExternalTaskSensor

DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 8, 18),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

DAG_NAME = "DATAMART_JOB"

DAG_ID = DAG(dag_id=DAG_NAME,
           default_args=DEFAULT_ARGS,
           schedule_interval='@daily')

WAIT_FOR_ATOMIC_A1 = ExternalTaskSensor(
    task_id='wait_for_task',
    external_dag_id='ATOMIC_JOB',
    external_task_id='get_file_sample',
    dag=DAG_ID)
