import requests

# Replace this with your actual Databricks API token
databricks_api_token = "${{ secrets.DATABRICKS_API_TOKEN }}"

url = "https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/list"
payload = ""
headers = {
  'Authorization': f'Bearer {databricks_api_token}'
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)

