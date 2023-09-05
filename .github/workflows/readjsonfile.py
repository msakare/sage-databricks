import json
 
# Opening JSON file
f = open('./api_response.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
print(data)
# Iterating through the json
# list
for i in data['job_id']:
    print(i)
 
# Closing file
f.close()
