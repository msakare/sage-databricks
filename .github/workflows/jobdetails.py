# apicall.py

import argparse
import requests

# Replace these placeholders with your actual Databricks API endpoints and token
databricks_api_url = "https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/list"
databricks_api_token = "dapic100eda776087528cd6a82f7ca84914a"

# Define command-line argument for job ID
parser = argparse.ArgumentParser(description="Fetch Databricks Job Details")
parser.add_argument("job_id", type=int, help="Databricks Job ID")
args = parser.parse_args()

# Construct the API request URL
job_details_url = f"{databricks_api_url}/{args.job_id}"

# Set the API request headers
headers = {
    "Authorization": f"Bearer dapic100eda776087528cd6a82f7ca84914a"
}

# Make the API request to get job details
response = requests.get(job_details_url, headers=headers)

if response.status_code == 200:
    job_details = response.json()
    print("Job Details:")
    print(f"Name: {job_details['settings']['name']}")
    print(f"Description: {job_details['settings']['description']}")
    # Add more job details as needed
else:
    print("Error fetching job details.")
