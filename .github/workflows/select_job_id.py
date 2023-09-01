# import requests

# databricks_api_token = "dapic100eda776087528cd6a82f7ca84914a"

# url = "https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/get?job_id=496296034538647"

# payload={}
# headers = {
#   'Authorization': f'Bearer {databricks_api_token}'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

# select_job_id.py

import sys
import json

current_directory = os.getcwd()

file_path = os.path.join(current_directory, 'downloaded_api_response.json')

# Read job IDs from the api_response.json artifact
try:
    with open(file_path, 'r') as file:
        response_data = json.load(file)
        job_ids = response_data.get('job_ids', [])
except FileNotFoundError:
    print("Error: api_response.json not found. Please run the previous steps to obtain job IDs.")
    sys.exit(1)

if not job_ids:
    print("No job IDs found in the api_response.json artifact.")
    sys.exit(1)

# Display available job IDs to the user
print("Available Job IDs:")
for i, job_id in enumerate(job_ids, start=1):
    print(f"{i}. {job_id}")

# Prompt the user to select a job ID
try:
    selected_index = int(input("Enter the number corresponding to the desired Job ID: ")) - 1
    if 0 <= selected_index < len(job_ids):
        selected_job_id = job_ids[selected_index]
        print(f"Selected Job ID: {selected_job_id}")
    else:
        print("Invalid selection. Please enter a valid number.")
except ValueError:
    print("Invalid input. Please enter a valid number.")


