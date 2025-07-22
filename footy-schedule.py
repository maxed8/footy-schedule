import requests

# TODO: get FA Cup and League One schedules - maybe separate api or web-scraping?

competitions = {
    'Premier League': 'PL',
    'Champions League': 'CL',
    'Serie A': 'SA',
    'Bundesliga': 'BL1',
    'La Liga': 'PD',
    'Ligue 1': 'FL1'
}

teams = {
    'Premier League': {
        'Manchester United FC',
        'Chelsea FC',
        'Arsenal FC',
        'Manchester City FC',
        'Tottenham Hotspur FC',
        'Liverpool FC',
        'Aston Villa FC',
        'Nottingham Forest FC',
        'Brighton & Hove Albion FC'
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
        'FC Barcelona',
        'Real Madrid CF',
        'Club Atlético de Madrid'
    },
    'Bundesliga': {
        'Bayer 04 Leverkusen',
        'Borussia Dortmund',
        'FC Bayern München'
    },
    'Serie A': {
        'AC Milan',
        'FC Internazionale Milano',
        'SSC Napoli',
        'Juventus FC',
        'Atalanta BC'
    },
    'Ligue 1': {
        'Paris Saint-Germain FC',
        'Olympique de Marseille'
    }
}


headers = { 'X-Auth-Token': '66354c8ea27b4b57904f7bd5541fc6f6' }

schedule = {key: [] for key in competitions.keys()}

# TODO: figure out this week's matchweek for each league

for name, code in competitions.items():
    if code == 'CL':
        uri = f'https://api.football-data.org/v4/competitions/{code}/matches'
    else:
        uri = f'https://api.football-data.org/v4/competitions/{code}/matches?matchday=23'

    response = requests.get(uri, headers=headers)
    data = response.json()

    if 'matches' in data:
        for match in response.json()['matches']:
            if code == 'CL':
                if match['matchday'] == 7:
                    schedule[name].append((match['homeTeam']['name'], match['awayTeam']['name'], match['utcDate']))
            else:
                schedule[name].append((match['homeTeam']['name'], match['awayTeam']['name'], match['utcDate']))
    else:
        print(f'Error: API request failed with status code {response.status_code}')
    

    
# print(matches)

print('Good Games')
print('-----------------')
for comp, matches in schedule.items():
    for match in matches:
        if match[0] in teams[comp] and match[1] in teams[comp]:
            print(match[0] + ' vs. ' + match[1] + ' at ' + match[2])






