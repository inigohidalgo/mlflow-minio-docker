import mlflow

mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")

with open("hello.txt", "w") as f:
    f.write("Hello world")

with mlflow.start_run():
    mlflow.log_params({"a": 1})
    mlflow.log_artifact("hello.txt", artifact_path="test")
    