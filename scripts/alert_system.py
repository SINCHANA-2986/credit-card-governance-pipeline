import pandas as pd
from google.cloud import bigquery
from datetime import datetime

df = pd.read_csv("data/creditcard.csv")
client = bigquery.Client()

threshold = 2
alerts = []

for col in df.columns:
    null_percent = (df[col].isnull().sum() / len(df)) * 100

    status = "PASS"
    if null_percent > threshold:
        status = "FAIL"

    alerts.append({
        "check_name": f"{col}_null_check",
        "status": status,
        "issue_count": int(df[col].isnull().sum()),
        "run_timestamp": datetime.utcnow()
    })

alerts_df = pd.DataFrame(alerts)

table_id = "fraud-governance-project.fraud_governance.quality_dashboard"

job = client.load_table_from_dataframe(
    alerts_df,
    table_id,
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
)

job.result()

print("Quality dashboard uploaded successfully")