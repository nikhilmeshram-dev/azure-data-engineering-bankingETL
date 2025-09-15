# Banking ETL Data Pipeline using Azure & Delta Lake (Medallion Architecture)
## Project Overview
This project demonstrates an **end-to-end ETL pipeline for the Banking domain**, handling **customer, transactions, and loan data** . It ingests data from multiple sources, performs robust transformations and quality checks, and delivers curated datasets for reporting, regulatory compliance, and fraud analytics.

## Business Problem
Banking data was **scattered across multiple sources** (CSV, APIs, JSON), causing  **inconsistent reporting, audit challenges, and poor fraud detection** . 
This project centralizes data, ensures **regulatory compliance**, and improves **fraud/risk monitoring** with optimized ETL.

## Key Features
-  **Incremental Loading** → Avoids full refresh, reduces cost and runtime.
-  **Delta Lake** → ACID, schema evolution & time travel.
-  **SCD Type 1 & Type 2** → Historical tracking to satisfy audit & compliance.
-  **Star Schema Design** → FactTransactions + DimCustomer, DimAccount, DimLoan.
-  **Fraud Detection Rules** → Inline risk flags during transformation.
-  **Medallion Architecture** → Bronze → Silver → Gold for modular processing.
-  **Secure Secrets** → Azure Key Vault + Managed Identity.

## Architecture overview
<img width="1569" height="880" alt="new" src="https://github.com/user-attachments/assets/092131ac-01a9-4baf-8f09-88f9b5084820" />

## ETL Flow 
- **Extract** → Data ingested from CSV (Accounts), JSON (Loan Applications), APIs (Transactions, KYC).
- **Transform** → Data cleaning, deduplication, standardization, incremental loading, SCD Type 1 & 2, fraud/risk tagging.
- **Load** → Curated Delta Lake tables in Gold layer (Star Schema) for reporting & analytics.

## Data Model (Star Schema)


## Technologies Used
- **Azure Data Factory** → Data ingestion and Pipeline orchestration
- **Azure Data Lake Storage** → Bronze/Silver/Gold layers
- **Azure Databricks (PySpark)** → Data transformations
- **Delta Lake** → ACID + schema evolution
- **Azure Synapse Analytics** → Data warehouse
- **Power BI** → BI dashboards

## Challenges & Solutions
**Data Quality & Schema Drift**
- *Problem*: Source files had missing values, duplicates, and evolving schema.
- *Solution*: Used **PySpark transformations** for null handling, deduplication, and enabled **schema evolution in Delta Lake**.

**Secure Access & Secrets Management**
- *Problem*: Storing keys and connection strings directly posed a security risk.
- *Solution*: Integrated **Azure Key Vault** and **Managed Identity** for secure, seamless authentication.

## Outcome
- Delivered a banking-grade ETL pipeline ready for **regulatory reporting, fraud detection, and business analytics**.
- Reduced runtime/cost significantly through incremental loads and optimized transformations.
- Enabled Power BI dashboards for Customer Analytics, Loan Performance, and Fraud Monitoring.

