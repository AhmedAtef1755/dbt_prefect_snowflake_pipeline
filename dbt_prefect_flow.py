from prefect import flow, task
import subprocess
import os

DBT_PROJECT_PATH = os.path.join(os.getcwd())

@task
def dbt_run():
    """Run dbt models"""
    print("🚀 Running dbt models...")
    result = subprocess.run(
        ["dbt", "run", "--project-dir", DBT_PROJECT_PATH],
        capture_output=True,
        text=True,
        shell=True
    )
    print(result.stdout)
    if result.returncode != 0:
        raise Exception("❌ dbt run failed!")

@task
def dbt_test():
    """Run dbt tests"""
    print("🧪 Running dbt tests...")
    result = subprocess.run(
        ["dbt", "test", "--project-dir", DBT_PROJECT_PATH],
        capture_output=True,
        text=True,
        shell=True
    )
    print(result.stdout)
    if result.returncode != 0:
        raise Exception("❌ dbt test failed!")

@flow(name="DBT Snowflake Prefect Flow")
def dbt_snowflake_flow():
    """Prefect flow to run dbt run and test"""
    dbt_run()
    dbt_test()

if __name__ == "__main__":
    dbt_snowflake_flow()
