# import http.client

# # conn = http.client.HTTPSConnection('v3.football.api-sports.io')
# conn = http.client.HTTPSConnection("soccer-football-info.p.rapidapi.com")

# headers = {
#     'x-rapidapi-host': "soccer-football-info.p.rapidapi.com",
#     'x-rapidapi-key': "1c22779388msh403ebc6a53cb061p142d96jsn6f176cecd18e"
# }

# conn.request('GET', '/leagues', headers=headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode('utf-8'))


import http.client
import ssl

# TODO: find better long-term solution
ssl._create_default_https_context = ssl._create_unverified_context

conn = http.client.HTTPSConnection("soccer-football-info.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "1c22779388msh403ebc6a53cb061p142d96jsn6f176cecd18e",
    'x-rapidapi-host': "soccer-football-info.p.rapidapi.com"
}

conn.request("GET", "/matches/view/basic/?i=90a218c1eac4c020&l=en_US", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))



