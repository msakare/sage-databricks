import json
 
# Opening JSON file
f = open('./api_response.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
print(data['jobs'])
job_data = (data['jobs'])
# Iterating through the json
# list
# for i in data['job_id']:
#     print(i)
 
# Closing file
f.close()


# Output the job IDs as an environment variable
print(f"::set-output name=job_ids::{job_ids}")
