# Mlflow on MinIO and docker

1. Ensure you have a `docker/config.env` with the necessary config keys
(any `${VARIABLE}` in the `docker/docker-compose.yml` file)

2. `tasks/docker-start.sh`

3. `python -m pip install -r requirements.txt`

4. Update connection variables in `create_study.py`

5. `python run_trials.py`

6. Check run in mlflow tracking URL
