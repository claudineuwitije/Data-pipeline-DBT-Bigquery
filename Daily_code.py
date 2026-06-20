#OPENTRACE
#pulling out the latest github update for a project


#checking the current github conneted 
git config user.email 

#checking the global github account 
git config --global user.email    

#switching the github account 
git config user.email "claudine.opentrace@gmail.com"  

#checking the git branch
 git branch 

#checking the status 
git status

# temporarily saves uncommitted changes 
git stash  

#switching to the main branch
git checkout main 

#pulling the latest version of the main branch
git pull

#creating a new branch 
git checkout -b DPL32       # here DPL32 is the branch

##EXAMPLE OF WORKFLOW 

git stash # temporarily saves uncommitted changes 

git checkout main  #switching to the main branch

git pull #pulling the latest version of the main branch

git checkout -b DPL32     #creating a new branch   # here DPL32 is the main branch


git stash pop # Restore your work  # In this case restore them on the new branch DPL32


#CREATE VIRTUAL ENVIRONMENT 
python3 -m venv venv  # HERE THE NAME OF THE VM is venv

#ACTIVATE the VM
.\venv\Scripts\activate   
                        # where venv is the name of the virtual environment,
                        # in our case , the name is "healthcareproject"

# In the new environment created, install the following in this order for dbt project 
pip install -r requirement.txt   # install dbt Dependencies such as dbt-core , pandas, google-cloud-bigquery etc.

python data/local/scripts/bq_schema_catalog.py # Run the BigQuery Schema Catalog Script # for example this may 
#1. Connects to BigQuery 
#2. Reads datasets/tables
#3. Extracts schema metadata
#4. Generates a catalog file

python data/local/scripts/generate_dbt_sources.py --refresh  # Generate dbt Sources its like update or generating the source.yml file 

python data/local/scripts/generate_dbt_model_from.py  # Generate dbt Models


## Installing DBT on local computer  or prequisit for installing dbt

#step 1. First to install Google Cloud SDK open PowerShell and run:
(New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")
& "$env:Temp\GoogleCloudSDKInstaller.exe"

# step 1 --> This will download and launch the installer for the Google Cloud SDK. Just go through the setup with default options.

# step 2. And then to authenticate with OAuth open Command Prompt (cmd) and run:
gcloud auth application-default login --scopes=https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform
# step 2 --> This will open a browser ask you to log in with your Google account and grant access for BigQuery and stuff just accept everything.


