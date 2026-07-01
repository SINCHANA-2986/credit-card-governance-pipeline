import pandas as pd
from google.cloud import bigquery
from datetime import datetime

client = bigquery.Client()

lineage_df = pd.DataFrame([{
    "source_file": "creditcard.csv",
    "target_table": "raw_transactions",
    "load_timestamp": datetime.utcnow(),
    "record_count": 284807
}])

table_id = "fraud-governance-project.fraud_governance.lineage_tracker"

job = client.load_table_from_dataframe(
    lineage_df,
    table_id,
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
)

job.result()

print("Lineage logged successfully")