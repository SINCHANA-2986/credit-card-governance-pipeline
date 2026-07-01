import pandas as pd
from google.cloud import bigquery

df = pd.read_csv("data/creditcard.csv")
client = bigquery.Client()

metadata = []

for col in df.columns:
    metadata.append({
        "column_name": col,
        "data_type": str(df[col].dtype),
        "source": "creditcard.csv",
        "update_frequency": "daily",
        "owner": "Fraud Team",
        "description": f"{col} column"
    })

metadata_df = pd.DataFrame(metadata)

table_id = "fraud-governance-project.fraud_governance.metadata_catalog"

job = client.load_table_from_dataframe(
    metadata_df,
    table_id,
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
)

job.result()

print("Metadata catalog uploaded successfully")