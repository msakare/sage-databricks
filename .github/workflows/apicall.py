import requests
import json
import os

def main():
    headers = {
        "Authorization": f"Bearer {os.getenv('#token')}"
    }
    source_env = os.getenv('dev')
    target_env = os.getenv('test')

    response = requests.get("https://sagerx-aws-devtest-comm.cloud.databricks.com", headers=headers, data=payload)
    print(response.text)
    requests_data  = response.request.body
    response_data = response.json()

  if __name__ == "__main__":
     main()
