from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

args = {
    "owner": "Airflow",
    "start_date": datetime(2022, 3, 5),
    "depends_on_past": False,
}

dag = DAG(
    dag_id="scheduler_interval_101",
    schedule_interval="* * * * *",
    default_args=args,
    catchup=False,
    tags=["example"],
)

hello_my_task = BashOperator(
    task_id="hello_task",
    bash_command='echo "hello from job 1."',
    dag=dag,
)
