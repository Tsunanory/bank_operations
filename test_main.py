import json
from main import processing

with open('operations.json') as file:
    prepared = json.load(file)
    executed = [x for x in prepared if x.get('state', '') == 'EXECUTED']

last_executed = sorted(executed, key=lambda x: x.get('date', ''))
one = last_executed[0]


