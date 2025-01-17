import requests
import json
import feedparser
import ssl
from bs4 import BeautifulSoup

# URL for BBC League One fixtures
# url = "https://www.bbc.co.uk/sport/football/league-one/scores-fixtures"

# # Fetch the page
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
# print(soup)

# # Extract match fixtures
# matches = []
# for fixture in soup.find_all("div", class_="qa-match-block"):
#     date = fixture.find("span", class_="gs-u-display-none gs-u-display-block@m qa-match-date").text.strip()
#     teams = [team.text.strip() for team in fixture.find_all("span", class_="sp-c-fixture__team-name")]
#     if teams:
#         matches.append({"date": date, "teams": " vs ".join(teams)})

# # Print fixtures
# for match in matches:
#     print(f"{match['date']}: {match['teams']}")


# import http.client
# import ssl
# import json

# # TODO: find better long-term solution
# ssl._create_default_https_context = ssl._create_unverified_context

# conn = http.client.HTTPSConnection("soccer-football-info.p.rapidapi.com")

# headers = {
#     'x-rapidapi-key': "1c22779388msh403ebc6a53cb061p142d96jsn6f176cecd18e",
#     'x-rapidapi-host': "soccer-football-info.p.rapidapi.com"
# }

# # conn.request("GET", "/matches/day/basic/?d=20250104&p=2&l=en_US", headers=headers)
# # conn.request("GET", "/matches/by/basic/?s=423f669ed2e3e1bf&l=en_US&m=5fb962e4a89ab6bd&p=1&c=1dd08ad826affff0", headers=headers)
# # conn.request("GET", "/championships/list/?p=1&c=all&l=en_US", headers=headers)

# res = conn.getresponse()
# data = res.read()

# parsed_data = data.decode()
# response_json = json.loads(parsed_data)
# print(response_json)


# with open('resp.text', 'w', encoding='utf-8') as file:
#     # for match in response_json.get('result', []):
#     #     league_name = match.get('championship', {}).get('name', 'Unknown League')

#     #     teamA_name = match.get('teamA', {}).get('name', 'Unknown Team A')
#     #     teamB_name = match.get('teamB', {}).get('name', 'Unknown Team B')

#     #             # Write to the file
#     #     file.write(f"League: {league_name}\n")
#     #     file.write(f"Team A: {teamA_name}\n")
#     #     file.write(f"Team B: {teamB_name}\n")
#     #     file.write("\n")  # Add a newline between matches

#     file.write(parsed_data)

# # Try decoding the data as JSON
# # try:
# #     parsed_data = json.loads(data.decode()) 
# #     print(parsed_data['result'])

# #      # Decode bytes and parse as JSON
# #     # print(json.dumps(parsed_data, indent=4))  # Pretty-print the JSON to see its structure
# # except json.JSONDecodeError as e:
# #     print("Failed to decode JSON:", e)
# # print("hello there")
# # print(data[0][0])
# # decoded = data.decode("utf-8")
# # print(decoded.result[0])

# # print(data.decode("utf-8"))



