from datetime import datetime, timedelta
from airflow import DAG
from airflow.models import Variable
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email_operator import EmailOperator


from etl_pipeline import _load, _transform, _unzip
import os

HOME = os.environ.get("HOME")
"""
    Current Link : "https://zenodo.org/record/3227177/files/OpenStack.tar.gz?download=1"
    I'll get this from the airflow metadata database.
"""
VAR = Variable.get("ETL_PIPELINE", deserialize_json=True)
LINK = VAR["LINK"]
TO_EMAIL = VAR["TO_EMAIL"]
FILES_PATH = os.path.join(HOME, 'airflow', 'dags', 'etl_pipeline')

args = {
    'owner': 'airflow',
    "retries": 1,
    'start_date': datetime(2021, 10, 26),
    "retry_delay": timedelta(minutes=1),
    'email': TO_EMAIL,
    'email_on_failure': True,
}

dag = DAG(
    'ETL_Pipeline',
    schedule_interval="@once",
    default_args=args,
    catchup=False,
    description="A DAG to perform ETL on data from OpenStack Logs.",
    template_searchpath=[
        FILES_PATH,
        os.path.join(HOME, 'data')
    ]
)

download_logs = BashOperator(
    task_id="download",
    bash_command="bash {} {} {}".format(
        os.path.join(FILES_PATH, '_download.sh'), HOME, LINK),
    dag=dag
)

check_file_downloaded = FileSensor(
    task_id="check_file",
    poke_interval=10,
    filepath=os.path.join(HOME, 'data', "data.tar.gz"),
    dag=dag
)

unzip_logs = PythonOperator(
    task_id='unzip',
    python_callable=_unzip.run,
    op_kwargs={'HOME': HOME},
    dag=dag
)

transform = PythonOperator(
    task_id='transform',
    python_callable=_transform.run,
    op_kwargs={'HOME': HOME},
    dag=dag
)

load_create_file = PythonOperator(
    task_id='load',
    python_callable=_load.run,
    op_kwargs={'HOME': HOME},
    dag=dag
)

create_table = MySqlOperator(
    task_id='create_mysql_table',
    mysql_conn_id="mysql_conn",
    sql='create_table.sql',
    dag=dag
)

execute_load = MySqlOperator(
    task_id='insert_into_table',
    mysql_conn_id="mysql_conn",
    sql='load_data.sql',
    dag=dag
)

clear_files = BashOperator(
    task_id="clear",
    bash_command="bash {} {}".format(
        os.path.join(FILES_PATH, '_clear.sh'),
        HOME),
    dag=dag
)

on_success_email = EmailOperator(
    task_id="success_email",
    to=TO_EMAIL,
    subject="Airflow Success: OpenStack ETL",
    html_content="<h2> Airflow <span style=\"color: rgb(75, 181, 67)\">Success</span>: OpenStack ETL at {} {} </h2>".format(
        str(datetime.now()), str(datetime.today().strftime('%A'))),
    dag=dag
)


download_logs >> check_file_downloaded >> unzip_logs >> transform >> load_create_file >> create_table >> execute_load >> clear_files >> on_success_email
