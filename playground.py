import requests

uri = 'https://api.football-data.org/v4/competitions/CL/matches'
headers = { 'X-Auth-Token': '66354c8ea27b4b57904f7bd5541fc6f6' }
response = requests.get(uri, headers=headers)
resp_data = response.json()

for match in resp_data['matches']:
    print(match['matchday'])
    print(match['homeTeam']['name'] + ' vs. ' + match['awayTeam']['name'])


# uri = 'https://api.football-data.org/v4/competitions/FAC/matches'
# headers = { 'X-Auth-Token': '66354c8ea27b4b57904f7bd5541fc6f6' }
# response = requests.get(uri, headers=headers)
# resp_data = response.json()
# print(resp_data)

# for match in resp_data['matches']:
#     print(match['matchday'])
#     print(match['homeTeam']['name'] + ' vs. ' + match['awayTeam']['name'])





