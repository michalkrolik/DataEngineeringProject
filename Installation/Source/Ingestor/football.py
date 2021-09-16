import http.client, json, os, datetime, pymongo

file_path = '/app/footballers.json'
#file_path = '/home/mike/Desktop/API-Football/footballers.json'

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "<the_Key>"
    }

players_id = [154, 278, 521, 874]
players = {}

for player_id in players_id:
    conn.request("GET", "/players?id="+str(player_id)+"&season=2021", headers=headers)

    res = conn.getresponse()
    data = res.read()
    players[player_id] = data.decode("utf-8")


with open(file_path, 'w') as file:
    file.write('{"data": [')
    file.close()

for key, value in players.items():
    with open(file_path, 'a') as file:
        file.write(f"{value},")
        
with open(file_path, 'rb+') as filehandle:
    filehandle.seek(-1, os.SEEK_END)
    filehandle.truncate()

with open(file_path, 'a') as file:
    file.write(']}')
    file.close()

with open(file_path) as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

f_name = {}
f_photo = {}
f_age = {}
f_country = {}
f_team = {}
f_goals = {}
f_assists = {}
f_appearences = {}
f_minutes_played = {}
f_cards_yellow = {}
f_cards_red = {}
f_penalty_scored = {}
f_penalty_missed = {}

for x in range(0, 4):
    for player in jsonObject['data'][x]:
        name = jsonObject['data'][x]['response'][0]['player']['name']
        photo = jsonObject['data'][x]['response'][0]['player']['photo']
        age = jsonObject['data'][x]['response'][0]['player']['age']
        country = jsonObject['data'][x]['response'][0]['player']['nationality']
        team = jsonObject['data'][x]['response'][0]['statistics'][0]['team']['name']
        goals = jsonObject['data'][x]['response'][0]['statistics'][0]['goals']['total']
        assists = jsonObject['data'][x]['response'][0]['statistics'][0]['goals']['assists']

        appearences = jsonObject['data'][x]['response'][0]['statistics'][0]['games']['appearences']
        minutes_played = jsonObject['data'][x]['response'][0]['statistics'][0]['games']['minutes']

        cards_yellow = jsonObject['data'][x]['response'][0]['statistics'][0]['cards']['yellow']
        cards_yellowred = jsonObject['data'][x]['response'][0]['statistics'][0]['cards']['yellowred']
        cards_red = jsonObject['data'][x]['response'][0]['statistics'][0]['cards']['red']

        penalty_scored = jsonObject['data'][x]['response'][0]['statistics'][0]['penalty']['scored']
        penalty_missed = jsonObject['data'][x]['response'][0]['statistics'][0]['penalty']['missed']
        
        f_name[name] = name
        f_photo[name] = photo
        f_age[name] = age
        f_country[name] = country
        f_team[name] = team
        f_goals[name] = goals
        f_assists[name] = assists
        f_appearences[name] = appearences
        f_minutes_played[name] = minutes_played
        f_cards_yellow[name] = cards_yellow
        f_cards_red[name] = cards_red
        f_penalty_scored[name] = penalty_scored
        f_penalty_missed[name] = penalty_missed


from collections import defaultdict

f_players = defaultdict(list)

for d in (f_name, f_photo, f_age, f_country, f_team, f_goals, f_assists, f_appearences, f_minutes_played, f_cards_yellow, f_cards_red, f_penalty_scored, f_penalty_missed): # you can list as many input dicts as you want here
    if d == f_name:
        for key, value in d.items():
            f_players[key].append('"Name":"'+str(value)+'"')
    if d == f_photo:
        for key, value in d.items():
            f_players[key].append('"Photo":"'+str(value)+'"')
    if d == f_age:
        for key, value in d.items():
            f_players[key].append('"Age":"'+str(value)+'"')
    if d == f_country:
        for key, value in d.items():
            f_players[key].append('"Country":"'+str(value)+'"')
    if d == f_team:
        for key, value in d.items():
            f_players[key].append('"Team":"'+str(value)+'"')
    if d == f_goals:
        for key, value in d.items():
            f_players[key].append('"Goals":"'+str(value)+'"')
    if d == f_assists:
        for key, value in d.items():
            f_players[key].append('"Assists":"'+str(value)+'"')
    if d == f_appearences:
        for key, value in d.items():
            f_players[key].append('"Appearences":"'+str(value)+'"')
    if d == f_minutes_played:
        for key, value in d.items():
            f_players[key].append('"Minutes_played":"'+str(value)+'"')
    if d == f_cards_yellow:
        for key, value in d.items():
            f_players[key].append('"Yellow_cards":"'+str(value)+'"')
    if d == f_cards_red:
        for key, value in d.items():
            f_players[key].append('"Red_cards":"'+str(value)+'"')
    if d == f_penalty_scored:
        for key, value in d.items():
            f_players[key].append('"Penalty_scored":"'+str(value)+'"')
    if d == f_penalty_missed:
        for key, value in d.items():
            f_players[key].append('"Penalty_missed":"'+str(value)+'"')

with open(file_path, 'w') as file:
    file.write('{"data": [')
    file.close()

for key, value in f_players.items():
    with open(file_path, 'a') as file:
        raw = str(value).replace("'","").replace("[","{").replace("]","}")
        file.write(f"{raw},")
        
with open(file_path, 'rb+') as filehandle:
    filehandle.seek(-1, os.SEEK_END)
    filehandle.truncate()

with open(file_path, 'a') as file:
    file.write(']}')
    file.close()

ts = datetime.datetime.now().timestamp()
today = datetime.datetime.now() - datetime.timedelta(hours=1, minutes=0)
today_formatted = today.strftime('%Y%m%d')

with open(file_path) as jsonFile:
    jsonPlayers = json.load(jsonFile)
    jsonFile.close()

for idx, val in enumerate(jsonPlayers['data']):
    p_name = val['Name'].split(" ")[-1]
    output = '{"'+str(p_name)+'": {"timestamp": "'+str(ts)+'", "Photo": "'+val['Photo']+'", "Age": "'+val['Age']+'", "Country": "'+val['Country']+'", "Team": "'+val['Team']+'", "Goals": "'+val['Goals']+'", "Assists": "'+val['Assists']+'", "Appearences": "'+val['Appearences']+'", "Minutes_played": "'+val['Minutes_played']+'", "Yellow_cards": "'+val['Yellow_cards']+'", "Red_cards": "'+val['Red_cards']+'", "Penalty_missed": "'+val['Penalty_missed']+'", "Penalty_scored": "'+val['Penalty_scored']+'"}}'

    mydict = json.loads(output)
    for k, v in mydict.items():
            myclient = pymongo.MongoClient("mongodb://mongodb:27017/", username='ingestor', password='ingestor')
            mydb = myclient[p_name]
            mycol = mydb[p_name]

            x = mycol.insert_one(v)
