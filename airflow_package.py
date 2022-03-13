import airflow
from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import timedelta