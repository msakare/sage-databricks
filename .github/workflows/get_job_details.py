import requests

databricks_api_token = "dapic100eda776087528cd6a82f7ca84914a"

source_job_id = input("Enter the job ID to be migrated: ")

url = f"https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/{source_job_id}"
headers = {
    'Authorization': f'Bearer {databricks_api_token}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    job_details = response.json()
    # You can use the job_details to extract information about the job, if needed
    print("Job details:", job_details)
else:
    print("Failed to retrieve job details.")
