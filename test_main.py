import json
from main import processing

with open('operations.json') as file:
    prepared = json.load(file)
    executed = [x for x in prepared if x.get('state', '') == 'EXECUTED']

last_executed = sorted(executed, key=lambda x: x.get('date', ''))
one = last_executed[0]
two = last_executed[1]
three = last_executed[2]
four = last_executed[3]
five = last_executed[4]



# def test_processing():
#     for 