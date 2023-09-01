import requests

url = "https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/get?job_id=496296034538647"

payload={}
headers = {
  'Authorization': 'Bearer dapic100eda776087528cd6a82f7ca84914a’
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

