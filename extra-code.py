import requests
import json
import feedparser
import ssl
from bs4 import BeautifulSoup
import soccerdata as sd
import pandas as pd
from datetime import date, timedelta

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


# working playground w espn soccerdata
competitions = [
    'ENG-Premier League',
    'ESP-La Liga',
    'GER-Bundesliga',
    'ITA-Serie A',
    'FRA-Ligue 1',
    # 'UEFA-Champions League',
    # 'ENG-FA Cup',
    # 'ENG-League 2'
]

my_teams = [
    'Manchester United',
    'Crawley Town'
]
 
big_teams = {
    'Premier League': {
        'Manchester United',
        'Chelsea',
        'Arsenal',
        'Manchester City',
        'Tottenham Hotspur',
        'Liverpool',
        'Aston Villa',
        'Nottingham Forest',
        'Brighton & Hove Albion'
    },
    'Champions League': {
        'FC Barcelona',
        'Real Madrid CF',
        'Paris Saint-Germain FC',
        'Bayer 04 Leverkusen',
        'Borussia Dortmund',
        'FC Bayern München',
        'AC Milan',
        'FC Internazionale Milano',
        'Arsenal FC',
        'Manchester City FC',
        'Liverpool FC',
        'Aston Villa FC'
    },
    'La Liga': {
        'Barcelona',
        'Real Madrid',
        'Atlético Madrid'
    },
    'Bundesliga': {
        'Bayer Leverkusen',
        'Borussia Dortmund',
        'Bayern Munich'
    },
    'Serie A': {
        'AC Milan',
        'Internazionale',
        'Napoli',
        'Juventus',
        'Atalanta'
    },
    'Ligue 1': {
        'Paris Saint-Germain',
        'Marseille'
    },
}

today = pd.to_datetime(date.today() - timedelta(days=150))
week_from_today = pd.to_datetime(date.today() - timedelta(days=143))

start = today.tz_localize('UTC')
end = week_from_today.tz_localize('UTC')

espn = sd.ESPN()
# print('heyo')
# print(espn.leagues)

# espn = sd.ESPN(leagues="UEFA-Champions League", seasons="2024-25")
# print(espn)

espn = sd.ESPN(leagues=competitions, seasons='2024-25')
schedule = espn.read_schedule()

# Loop through each league and print all fixtures in date range
# for league in schedule.index.get_level_values("league").unique():
#     league_name = league.split('-')[-1]
#     print(f"\n📅 Fixtures for {league_name}:\n" + "-"*40)
#     fixtures = schedule.xs(league, level="league")
#     recent_fixtures = fixtures[(fixtures["date"] >= start) & (fixtures["date"] <= end)]

#     if recent_fixtures.empty:
#         print("No fixtures in range.")
#     else:
#         print(recent_fixtures[["date", "home_team", "away_team"]])



# big games here
print('\n📅 Big matches:\n' + "-"*60)
for league in schedule.index.get_level_values("league").unique():
    league_name = league.split('-')[-1]
    fixtures = schedule.xs(league, level="league")
    recent_fixtures = fixtures[(fixtures["date"] >= start) & (fixtures["date"] <= end)]

    if recent_fixtures.empty:
        print("No fixtures in range.")
    else:
        for _, match in recent_fixtures.iterrows():
            home_team, away_team, match_time = match['home_team'], match['away_team'], match['date']
            if home_team in my_teams or away_team in my_teams or (home_team in big_teams[league_name] and away_team in big_teams[league_name]):
                print(str(match_time) + ' : ' + home_team + ' vs. ' + away_team + '\n' + '-'*60)

# print(schedule.head())

# print(fixtures_on_date)
# fixtures_on_date = schedule[schedule['date'] == '2025-04-01']


# uri = 'https://api.football-data.org/v4/competitions/CL/matches'
# headers = { 'X-Auth-Token': '66354c8ea27b4b57904f7bd5541fc6f6' }
# response = requests.get(uri, headers=headers)
# resp_data = response.json()

# for match in resp_data['matches']:
#     print(match['matchday'])
#     print(match['homeTeam']['name'] + ' vs. ' + match['awayTeam']['name'])


# # uri = 'https://api.football-data.org/v4/competitions/FAC/matches'
# # headers = { 'X-Auth-Token': '66354c8ea27b4b57904f7bd5541fc6f6' }
# # response = requests.get(uri, headers=headers)
# # resp_data = response.json()
# # print(resp_data)

# # for match in resp_data['matches']:
# #     print(match['matchday'])
# #     print(match['homeTeam']['name'] + ' vs. ' + match['awayTeam']['name'])









