# Mlflow on MinIO and docker

1. Ensure you have a `docker/config.env` with the necessary config keys
(any `${VARIABLE}` in the `docker/docker-compose.yml` file)

2. `tasks/docker-start.sh`

3. Configure connection credentials

    i. PostgreSQL credentials

        1. Ensure the new postgresql instance has a user for the optuna db and a different one for the mlflow db
        2. Create a new database called optuna and another called mlflow (if they don't already exist)

    ii. MinIO credentials

        1. create a new access key either using `mc` CLI client or the console terminal (usually found at localhost:9001)
        2. create a new bucket called mlflow

    iii. Update `docker/config.env` with the newly-updated credentials
    iv. docker-compose down and repeate step `2.`
    iv. Update connection variables in `create_study.py`

4. `python -m pip install -r requirements.txt`


5. `python run_trials.py`

6. Check run in mlflow tracking URL
