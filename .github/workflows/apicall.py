import requests
import json
import os

def main():
    headers = {
        "Authorization": f"Bearer {os.getenv('#token')}"
    }
    source_env = os.getenv('SOURCE_ENV')
    target_env = os.getenv('TARGET_ENV')

    response = requests.get("#apiurl", headers=headers)
    requests_data  = response.request.body
    response_data = response.json()

  if __name__ == "__main__":
     main()
