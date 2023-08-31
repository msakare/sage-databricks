import requests

# Replace this with your actual Databricks API token
databricks_api_token = "dapic100eda776087528cd6a82f7ca84914a"

url = "https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/list"
payload = ""
headers = {
  'Authorization': f'Bearer {databricks_api_token}'
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)

