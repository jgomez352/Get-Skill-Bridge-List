import requests

url = "https://dodskillbridge.usalearning.gov/data/organizationsData.js"
#just a random link of a dummy file

r = requests.get(url)



#retrieving data from the URL using get method

with open("DoD SkillBridge Programs.json", 'wb') as f:
#giving a name and saving it in any required format
#opening the file in write mode

    filteredContent = r.content[11:len(r.content)-1]

    f.write(filteredContent)
#writes the URL contents from the server