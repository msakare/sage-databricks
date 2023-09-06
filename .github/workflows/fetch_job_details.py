

# import requests

# databricks_api_token = "dapic100eda776087528cd6a82f7ca84914a"

# # You can pass the job_id as a command line argument or read it from a file, depending on your workflow
# job_id = "496296034538647"  # Replace with the actual job ID

# url = f"https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/get?job_id={job_id}"

# payload = {}
# headers = {
#     'Authorization': f'Bearer {databricks_api_token}'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

# fetch_job_details.py

# import sys
# import requests

# databricks_api_token = "dapic100eda776087528cd6a82f7ca84914a"

# # Read the job ID as a command line argument
# if len(sys.argv) < 2:
#     print("Usage: python fetch_job_details.py <job_id>")
#     sys.exit(1)

# job_id = sys.argv[1]

# url = f"https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/get?job_id={job_id}"

# payload = {}
# headers = {
#     'Authorization': f'Bearer {databricks_api_token}'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)


import sys
import requests


databricks_api_token = "dapic100eda776087528cd6a82f7ca84914a"
url = "https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/get?job_id=496296034538647"

payload={}
headers = {
    'Authorization': f'Bearer {databricks_api_token}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)



