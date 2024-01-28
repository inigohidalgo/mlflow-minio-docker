import os

import optuna
from optuna.integration.mlflow import MLflowCallback
# import mlflow
import sklearn.datasets
import sklearn.ensemble
import sklearn.model_selection
import sklearn.svm

import create_study
from create_study import mlflow, mlflow_tracking_url, optuna_rdb_url

mlflc = MLflowCallback(
    tracking_uri=mlflow_tracking_url,
    metric_name="accuracy",
)



# FYI: Objective functions can take additional arguments
# (https://optuna.readthedocs.io/en/stable/faq.html#objective-func-additional-args).
def objective(trial):
        iris = sklearn.datasets.load_iris()
        x, y = iris.data, iris.target
  
        rf_max_depth = trial.suggest_int("rf_max_depth", 2, 100, log=True)
        rf_n_estimators = trial.suggest_int("rf_n_estimators", 2, 100, log=True)
        # mlflow.log_param('rf_max_depth', rf_max_depth)
        classifier_obj = sklearn.ensemble.RandomForestClassifier(
            max_depth=rf_max_depth, n_estimators=10
        )

        score = sklearn.model_selection.cross_val_score(classifier_obj, x, y, n_jobs=-1, cv=3)
        
        accuracy = score.mean()
        # mlflow.log_metric('accuracy', accuracy)
        return accuracy


if __name__ == "__main__":
    study_name = "test-optuna-005"
    study = optuna.create_study(
        study_name=study_name,
        storage=optuna_rdb_url,
        direction="maximize",
        sampler=optuna.samplers.TPESampler(),
        load_if_exists=True
    )

    # with mlflow.start_run():
    study.optimize(objective, n_trials=100, callbacks=[mlflc])
    print(study.best_trial)