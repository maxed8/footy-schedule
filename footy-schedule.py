import requests

competitions = {
    'FA Cup': 'FAC',
    'Premier League': 'PL',
    'Champions League': 'CL',
    'Serie A': 'SA',
    'Bundesliga': 'BL1',
    'La Liga': 'PD',
    'Ligue 1': 'FL1'
}

premTeams = {
    'Manchester United FC',
    'Chelsea FC',
    'Arsenal FC',
    'Manchester City FC',
    'Tottenham Hotspur FC',
    'Liverpool FC',
    'Aston Villa FC',
    'Nottingham Forest FC',
    'Brighton & Hove Albion FC'
}

uclTeams = {
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
}

laLigaTeams = {
    'FC Barcelona',
    'Real Madrid CF',
    'Club Atlético de Madrid'
}

bundesligaTeams = {
    'Bayer 04 Leverkusen',
    'Borussia Dortmund',
    'FC Bayern München'
}

serieATeams = {
    'AC Milan',
    'FC Internazionale Milano',
    'Juventus FC',
    'Atalanta BC'
}

ligueOneTeams = {
    'Paris Saint-Germain FC',
    'Olympique de Marseille'
}


headers = { 'X-Auth-Token': '66354c8ea27b4b57904f7bd5541fc6f6' }

for name, code in competitions.items():
    if code in {'FAC', 'CL'}:
        uri = f'https://api.football-data.org/v4/competitions/{code}/matches'
    else:
        uri = f'https://api.football-data.org/v4/competitions/{code}/matches?matchday=22'
    response = requests.get(uri, headers=headers)
    print(name)
    if code != 'CL' and code != 'FAC':
        for match in response.json()['matches']:
            print(match['homeTeam']['name'] + ' vs. ' + match['awayTeam']['name'])
        print('------------------------------------')
    else:
        print(response.json)
        print('------------------------------------')




