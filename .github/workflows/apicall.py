import requests
url = "https://sagerx-aws-devtest-comm.cloud.databricks.com/api/2.1/jobs/list"
payload = ""
headers = {
  'Authorization': 'Bearer ${{ secrets.DATABRICKS_API_TOKEN }}'
}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)
