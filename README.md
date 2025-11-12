# 📊 End-to-End Data Engineering Project: dbt, Snowflake & Prefect  


## 🚀 Overview  
This project is a **complete data engineering pipeline** using **dbt (Data Build Tool), Snowflake (Data Warehouse), and Prefect (Orchestration Tool)**. It covers **data transformation, testing, and workflow orchestration** in a structured and scalable manner.  

## 🛠️ Tech Stack  
- **dbt Core** – For SQL-based data transformation and modeling  
- **Snowflake** – Cloud-based data warehouse  
- **Prefect** – Workflow orchestration and automation  
- **Python** – Scripting and automation  
- **Git** – Version control  

## 📂 Project Structure
```bash
dbt_prefect_snowflake_pipeline/
│── analyses/
│── dataset/
│── dbt_internal_packages/
│── logs/
│── macros/
│── models/
│── seeds/
│── snapshots/
│── target/
│── tests/
│── dbt_prefect_flow.py        # Prefect flow to orchestrate dbt
│── dbt_project.yml             # dbt configuration file
│── requirements.txt            # Python dependencies
│── .gitignore
│── README.md
```
---
## ⚙️ Setup Instructions

1️⃣ Clone the repository:
```
git clone https://github.com/AhmedAtef1755/dbt_prefect_snowflake_pipeline.git
cd dbt_prefect_snowflake_pipeline
```

2️⃣ Set Up a Virtual Environment:
```
python -m venv venv
venv\Scripts\activate     # Windows
# or
source venv/bin/activate  # Mac/Linux

```

3️⃣ Install dependencies:
```
pip install -r requirements.txt

``` 
4️⃣ Configure dbt Connection to Snowflake:
```
snowflake_project:
  outputs:
    dev:
      type: snowflake
      account: your_account
      user: dbt_user
      password: your_password
      role: ACCOUNTADMIN
      database: finance_db
      warehouse: finance_wh
      schema: raw
  target: dev

```
---
## 🧠 Run the Pipeline
Step 1 – Start Prefect Server (UI)
```
prefect server start

``` 
Step 2 – Run the Prefect Flow
```
python dbt_prefect_flow.py

``` 
This will automatically:

Run dbt run to transform your models.

Run dbt test to validate data integrity.

You can monitor all runs in the Prefect UI.

## 📈 Future Improvements
Add automated scheduling using Prefect’s CronSchedule

Integrate data ingestion from external sources (API or S3)

Containerize with Docker for easier deployment

Deploy Prefect flow on Prefect Cloud