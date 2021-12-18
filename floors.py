import requests
import time 

projects = ['clonex-mintvial','clonex','adidasoriginals','terraforms','world-of-women-nft','bossbeauties','headdao','cdao','galaxyeggs9999','gauntlets','goatsoup','5555-hunter-orrell']

print('\n FLOOR PRICES\n')

for project in projects:

    headers = {"Accept": "application/json"}
    opensea = f'https://api.opensea.io/api/v1/collection/{project}/stats'

    r = requests.request("GET", opensea, headers=headers)

    data = r.json()

    floor = data['stats']['floor_price']

    print(f' {project}: {floor}\n')

    time.sleep(1)

print(' Done!')
