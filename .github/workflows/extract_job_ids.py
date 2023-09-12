import json
import sys

# Read the job list JSON from stdin
job_list_json = sys.stdin.read()

# Parse the JSON string to a Python dictionary
job_list = json.loads(job_list_json)

# Extract and print the job IDs
job_ids = [job["job_id"] for job in job_list["jobs"]]
for job_id in job_ids:
    print(job_id)
