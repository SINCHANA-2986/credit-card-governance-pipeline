# Credit Card Fraud Data Governance Pipeline

## Overview
An enterprise-style data governance pipeline built using Python and Google BigQuery over 285K+ financial transactions. This project focuses on data governance, stewardship, quality monitoring, and lineage tracking rather than predictive modeling.

## Architecture
Raw CSV → Python ETL → BigQuery Raw Table → Data Quality Checks → Metadata Catalog → Lineage Tracking → Quality Dashboard

## Features
- Data ingestion into BigQuery
- Null value checks
- Duplicate detection
- Schema validation
- Range validation for transaction amounts
- Metadata catalog creation
- Data lineage tracking
- Automated quality alert dashboard

## Tech Stack
- Python
- Pandas
- Google BigQuery
- SQL
- Google Cloud Platform

## Dataset
Credit Card Fraud Detection Dataset (Kaggle)

## Governance Components
### Data Quality
- Null checks
- Duplicate detection
- Schema validation
- Range validation

### Metadata Management
Maintains:
- Column names
- Data types
- Source information
- Ownership
- Update frequency

### Data Lineage
Tracks:
- Source file
- Target table
- Load timestamp
- Record count

### Alerting Dashboard
Monitors quality thresholds and records PASS/FAIL status.

## Results
- 285,807 records ingested
- 1081 duplicate records detected
- 0 null values found
- Fully governed BigQuery pipeline established

## Project Structure
```text
credit-card-governance/
│── scripts/
│── sql/
│── README.md
```