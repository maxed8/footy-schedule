import requests
import json
import soccerdata as sd
import pandas as pd
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

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

# espn = sd.ESPN()


espn = sd.ESPN(leagues=competitions, seasons='2024-25')
schedule = espn.read_schedule()

output = '\n📅 Big Matches This Week:\n' + "-"*49

big_matches = []
# big games here
for league in schedule.index.get_level_values("league").unique():
    league_name = league.split('-')[-1]
    fixtures = schedule.xs(league, level="league")
    recent_fixtures = fixtures[(fixtures["date"] >= start) & (fixtures["date"] <= end)]

    if not recent_fixtures.empty:
        for _, match in recent_fixtures.iterrows():
            home_team, away_team, match_time = match['home_team'], match['away_team'], match['date']
            if home_team in my_teams or away_team in my_teams or (home_team in big_teams[league_name] and away_team in big_teams[league_name]):
                big_matches.append((str(match_time), home_team, away_team))

# sort by date
big_matches.sort(key=lambda x: datetime.fromisoformat(x[0]))

eastern = ZoneInfo('America/New_York')

# format dates nicely and add to output
for match in big_matches:
    dt = datetime.fromisoformat(match[0])
    dt_est = dt.astimezone(eastern)
    match_time = dt_est.strftime('%a, %b %d at %-I:%M %p')
    home_team, away_team = match[1], match[2]
    output += match_time + ' : ' + home_team + ' vs. ' + away_team + '\n' + '-'*49
    
print(big_matches)

# for match in big_matches:
#     output += str(match_time) + ' : ' + home_team + ' vs. ' + away_team + '\n' + '-'*49

webhook_url = "https://hooks.slack.com/services/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"
payload = {"text": output}
headers = {'Content-Type': 'application/json'}

response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)





