import requests
url = "https://data.gov.sg/api/action/datastore_search?resource_id=9de30d8d-3c0d-48ab-8c1b-4a7dc03d687a&limit=5"
response = requests.get(url)
data = response.json()
print(data.keys())
print(data['result'].keys())
print(data['result'].values())

# records is embedded in another list 
print(data['result']['records'][0])
for each in data['result']['records']:
    #print(each)
    print(f"On {each['day_of_as_of_date']}, {each['count_of_case']} "
          f"deceased case(s) from age group: {each['age_groups']}")
