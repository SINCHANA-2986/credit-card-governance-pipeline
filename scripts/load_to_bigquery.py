from google.cloud import bigquery

client = bigquery.Client()

table_id = "fraud-governance-project.fraud_governance.raw_transactions"

schema = [
    bigquery.SchemaField("Time", "FLOAT64"),
]

# V1 to V28
for i in range(1, 29):
    schema.append(bigquery.SchemaField(f"V{i}", "FLOAT64"))

schema.extend([
    bigquery.SchemaField("Amount", "FLOAT64"),
    bigquery.SchemaField("Class", "INT64"),
])

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    schema=schema,
    write_disposition="WRITE_TRUNCATE"
)

with open("data/creditcard.csv", "rb") as source_file:
    load_job = client.load_table_from_file(
        source_file,
        table_id,
        job_config=job_config
    )

load_job.result()

print("CSV uploaded successfully")