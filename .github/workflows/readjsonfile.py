import json

# Opening JSON file
f = open('./api_response.json')

# returns JSON object as
# a dictionary
data = json.load(f)
job_data = data['jobs']

# Extracting job IDs and joining them into a comma-separated string
job_ids = ",".join(str(job['job_id']) for job in job_data)

# Closing file
f.close()

# Output the job IDs as an environment variable
print(f"::set-output name=job_ids::{job_ids}")

