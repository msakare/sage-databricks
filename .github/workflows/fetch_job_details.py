import requests

selected_job_id = input("Select a job ID: ")  # Input from the user

url = f"https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/get?job_id={selected_job_id}"

payload = {}
headers = {
    'Authorization': 'Bearer <TOKEN>'  # Replace <TOKEN> with your token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


# import sys
# import requests


# databricks_api_token = "dapic100eda776087528cd6a82f7ca84914a"
# url = "https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/get?job_id=496296034538647"

# payload={}
# headers = {
#     'Authorization': f'Bearer {databricks_api_token}'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)



