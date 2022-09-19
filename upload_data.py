import requests
# Change this with your URL
url = 'https://waterstones-data.s3.us-west-1.amazonaws.com/data.json'

response = requests.get(url)
with open('data.json', 'wb') as f:
    f.write(response.content)