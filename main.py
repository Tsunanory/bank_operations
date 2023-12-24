import json
from classes import operation

with open('operations.json') as file:
    prepared = json.load(file)
    executed = [x for x in prepared if x.get('state', '') == 'EXECUTED']

last_executed = sorted(executed, key=lambda x: x.get('date', ''), reverse=True)[:5]

def processing(ops):
    for note in ops:
        if note.get('from'):
            result = operation(note['date'], note['description'], note['from'], note['to'], 
                    note['operationAmount']['amount'], note['operationAmount']['currency']['name'])
            print(result)
            print( )
        else:
            result = operation(note['date'], note['description'], '', note['to'], 
                    note['operationAmount']['amount'], note['operationAmount']['currency']['name'])
            print(result)
            print( )

processing(last_executed)