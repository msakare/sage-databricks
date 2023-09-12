import requests
import os

# Get the selected source environment from GitHub Actions environment variables
source_environment = os.getenv("SOURCE")

# Replace with your Databricks API token stored as a GitHub secret
databricks_token = "dapic100eda776087528cd6a82f7ca84914a"

# Databricks API URL for Get Jobs List
url = f"https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/list""

headers = {
    'Authorization': f'Bearer {databricks_token}'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    job_list_json = response.text  # Get the JSON response
    print(job_list_json)  # Print the JSON response for debugging
    # Process the job list as needed
else:
    print(f"Failed to get job list. Status code: {response.status_code}")
