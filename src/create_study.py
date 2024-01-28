import mlflow
import optuna
# Replace these values with your PostgreSQL container details
username = "optuna"
password = "optuna"
host = "172.27.0.3"
port = 5432
database = "optuna"

mlflow_tracking_url = "http://127.0.0.1:5000"
# Construct the SQLAlchemy URL
optuna_rdb_url = f"postgresql://{username}:{password}@{host}:{port}/{database}"


def create_study():
    study_name = "test-optuna-004"
    mlflow.set_tracking_uri(uri=mlflow_tracking_url)

    mlflow.set_experiment(f"optuna__{study_name}")
    return optuna.create_study(
        study_name=study_name,
        storage=optuna_rdb_url,
        direction="maximize",
        sampler=optuna.samplers.TPESampler(),
        load_if_exists=True
    )


if __name__ == "__main__":
    # optuna.create_study(
    #     study_name=study_name,
    #     storage=url,
    #     direction="maximize",
    #     sampler=optuna.samplers.TPESampler()
    # )
    create_study()