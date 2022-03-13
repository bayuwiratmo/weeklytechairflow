default_args = {
    'owner': 'bayu wiratmo',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2),
    'email': ['bayu.wiratmo@yummycorp.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}