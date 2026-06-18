#Creating a bigquery projet for endto end dbt project 

Step 1: go to google cloud console --> create new project --> project name 
                                                  --> select organisation
                                                        #( make sure to select your organisation or no organisation. 
                                                        # if it just your own project select no organisation. this will enable to creation key late)
                                                  --> create
Step 2  : in the upper letf , select the project you created  then still in the upper left , click of the 3 - and select 
                                    --> sercice account --> create service account  --> service account name 
                                                                                    --> the service account ID is generated automatically 
                                                                                    --> service account description ( if needed)

                                                                                    --> permission ( in the rose select storage adm and add a new role as bigquery adm)
                                                                                    --> Princiapl with access ( here add people who you want to have access to the project)
                                                                                    --> once the service account is created , then click on it and go to the keys and add key and select JSON then create
                                                                                    
Step 3: creating bucket ( in our case we created mock data --> the code is provided in github)
        # note that the mok data created in the bucket are find in cloud storage--> bucket 

Step 4: Creating big qyery external tables  ( the code is in the github.)
        this create a view to the data stoared in the bucket so that you do not store the same ata in bigquery and pay twice

Step 5 : step up DBT cloud environement


Create a new project : --> project name 
                        -->  add your key generated as json file 
                        --> connect your github account and select your repo for the dbt project


# Creating a Google BigQuery Project and DBT Cloud Environment for an End-to-End Analytics Project

## Overview

This guide explains how to:

1. Create a Google Cloud Project
2. Create a Service Account
3. Generate Service Account Keys
4. Create a Cloud Storage Bucket
5. Upload Mock Data
6. Create BigQuery External Tables
7. Configure a DBT Cloud Project
8. Connect DBT Cloud to GitHub

---

# Architecture Overview

```text
                 ┌─────────────────┐
                 │     GitHub      │
                 │  dbt Project    │
                 └────────┬────────┘
                          │
                          │
                          ▼
                 ┌─────────────────┐
                 │    DBT Cloud    │
                 └────────┬────────┘
                          │
                          │ Service Account
                          ▼
                 ┌─────────────────┐
                 │    BigQuery     │
                 │   Data Models   │
                 └────────┬────────┘
                          │
                          │ External Tables
                          ▼
                 ┌─────────────────┐
                 │ Cloud Storage   │
                 │   Mock Data     │
                 └─────────────────┘
```

---

# Prerequisites

Before starting, ensure you have:

* A Google Account
* Access to Google Cloud Platform (GCP)
* A GitHub Account
* A DBT Cloud Account

Useful services:

* Google Cloud Console
* BigQuery
* Cloud Storage
* DBT Cloud
* GitHub

---

# Step 1: Create a Google Cloud Project

1. Open Google Cloud Console.

2. Click the Project Selector at the top of the page.

3. Click **New Project**.

4. Complete the project information:

| Field        | Example                              |
| ------------ | ------------------------------------ |
| Project Name | dbt-bike-share-project               |
| Organization | Your organization OR No Organization |

### Important

If this is a personal learning project:

* Select **No Organization**

If this project belongs to a company:

* Select the appropriate organization.

Some organizations restrict the creation of Service Account keys. Using **No Organization** for personal projects generally avoids these restrictions.

5. Click **Create**.

---

# Step 2: Select the New Project

After the project is created:

1. Click the project selector at the top of the page.
2. Select the newly created project.

Verify that the correct project name appears in the top navigation bar.

---

# Step 3: Enable Required APIs

Before creating resources, enable the required services.

Navigate to:

```text
APIs & Services
    → Library
```

Enable:

* BigQuery API
* Cloud Storage API
* IAM API

Wait until all services are enabled.

---

# Step 4: Create a Service Account

Navigate to:

```text
IAM & Admin
    → Service Accounts
```

Click:

```text
Create Service Account
```

Complete the form:

| Field                | Example                         |
| -------------------- | ------------------------------- |
| Service Account Name | dbt-service-account             |
| Service Account ID   | Auto-generated                  |
| Description          | Service Account for DBT Project |

Click:

```text
Create and Continue
```

---

# Step 5: Assign Roles

Grant the Service Account permissions.

Add the following roles:

| Role           | Purpose                                |
| -------------- | -------------------------------------- |
| BigQuery Admin | Manage BigQuery datasets and tables    |
| Storage Admin  | Access Cloud Storage buckets and files |

Click:

```text
Continue
```

---

# Step 6: Grant User Access (Optional)

If other users need access:

Add them under:

```text
Grant users access to this service account
```

Examples:

* Team members
* Instructors
* Project collaborators

Click:

```text
Done
```

---

# Step 7: Generate a Service Account Key

After the Service Account is created:

1. Click the Service Account.
2. Open the **Keys** tab.
3. Click:

```text
Add Key
    → Create New Key
```

4. Select:

```text
JSON
```

5. Click:

```text
Create
```

A JSON file will automatically download.

### Important

Keep this file safe.

This file will later be used by DBT Cloud to connect to BigQuery.

Example:

```text
dbt-service-account.json
```

Do not share this file publicly or upload it to GitHub.

---

# Step 8: Create a Cloud Storage Bucket

Navigate to:

```text
Cloud Storage
    → Buckets
```

Click:

```text
Create Bucket
```

Provide:

| Field         | Example                      |
| ------------- | ---------------------------- |
| Bucket Name   | dbt-bike-share-data          |
| Region        | Choose your preferred region |
| Storage Class | Standard                     |

Click:

```text
Create
```

---

# Step 9: Upload Mock Data

Generate the mock data using the scripts provided in the GitHub repository.

After generating the files:

1. Open the bucket.
2. Click:

```text
Upload Files
```

3. Upload the CSV files.

You can verify the upload by checking:

```text
Cloud Storage
    → Bucket
        → Uploaded Files
```

---

# Step 10: Create BigQuery External Tables

External Tables allow BigQuery to query files directly from Cloud Storage.

Benefits:

* No duplicate storage
* Lower costs
* Single source of truth

Architecture:

```text
CSV Files
    ↓
Cloud Storage Bucket
    ↓
External Table
    ↓
BigQuery Queries
```

Run the SQL scripts provided in the GitHub repository.

The scripts will:

* Create datasets
* Create external tables
* Connect BigQuery to files stored in Cloud Storage

Verify the tables appear under:

```text
BigQuery
    → Dataset
        → External Tables
```

---

# Step 11: Create a DBT Cloud Project

Log in to DBT Cloud.

Click:

```text
Create New Project
```

Provide:

| Field        | Example              |
| ------------ | -------------------- |
| Project Name | Bike Share Analytics |
| Warehouse    | BigQuery             |

---

# Step 12: Configure BigQuery Connection

During setup:

1. Choose:

```text
BigQuery
```

2. Authentication Method:

```text
Service Account JSON
```

3. Upload the JSON key created earlier.

DBT Cloud will use this Service Account to connect to BigQuery.

---

# Step 13: Connect GitHub Repository

In DBT Cloud:

1. Select:

```text
Connect Repository
```

2. Authenticate with GitHub.

3. Authorize DBT Cloud.

4. Select the repository containing your DBT project.

Example:

```text
github.com/username/dbt-bike-share-project
```

5. Click:

```text
Create Project
```

---

# Step 14: Verify Everything Works

Test the connection from DBT Cloud.

Verify:

✓ BigQuery Connection Successful

✓ Repository Connected

✓ Development Environment Created

✓ Models Visible

You are now ready to:

```text
dbt run
dbt test
dbt build
```

and build your end-to-end analytics project.

---

# Final Architecture

```text
                   GitHub Repository
                           │
                           ▼
                    ┌────────────┐
                    │ DBT Cloud  │
                    └──────┬─────┘
                           │
                Service Account JSON
                           │
                           ▼
                    ┌────────────┐
                    │ BigQuery   │
                    └──────┬─────┘
                           │
                    External Tables
                           │
                           ▼
                    ┌────────────┐
                    │ Cloud      │
                    │ Storage    │
                    └────────────┘
```
