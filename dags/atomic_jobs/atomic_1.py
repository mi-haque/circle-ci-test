from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.sensors.gcs_sensor import GoogleCloudStorageObjectSensor

DAG_NAME = "ATOMIC_JOB"
GCS_CONN = "GCS_KEY"
BUCKET = "external_sensor_check"
OBJECT = "destination/sample.png"

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

DAG_ID = DAG(dag_id=DAG_NAME,
             default_args=DEFAULT_ARGS,
             schedule_interval='@daily')

SENSE = GoogleCloudStorageObjectSensor(
    task_id='get_file_sample',
    dag=DAG_ID,
    bucket=BUCKET,
    object=OBJECT,
    google_cloud_conn_id=GCS_CONN,
)

PRINT = BashOperator(
    task_id='print',
    bash_command='echo "file arrived"',
    params={'my_param': 'dummy param'},
    dag=DAG_ID)

SENSE > PRINT
