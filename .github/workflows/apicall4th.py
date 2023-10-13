import sys
import requests

# Get the selected job ID from command line arguments
selected_job_id = sys.argv[1]

# Construct the API request URL with the selected job ID
url = f"https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/get?job_id={selected_job_id}"

# Make the API request
response = requests.get(url, headers=headers, data=payload)

# Process the API response as needed
print(response.text)

