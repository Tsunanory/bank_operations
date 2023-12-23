from classes import operation
import json

with open('operations.json') as file:
    prepared = json.load(file)
    executed = [x for x in prepared if x.get('state', '') == 'EXECUTED']

last_executed = sorted(executed, key=lambda x: x.get('date', ''), reverse=True)
one = last_executed[1]
two = last_executed[0]


def test_prepare_source():
    test = operation(one['date'], one['description'], one['from'],
                     one['to'], one['operationAmount']['amount'],
                     one['operationAmount']['currency']['name'])
    assert test.prepare_source(one['from']) == 'Visa Classic 2842 87** **** 9012'
    test = operation(two['date'], two['description'], two['from'],
                     two['to'], two['operationAmount']['amount'],
                     two['operationAmount']['currency']['name'])
    assert test.prepare_source(two['from']) == ''

def test_prepare_destination():
    test = operation(one['date'], one['description'], one['from'],
                     one['to'], one['operationAmount']['amount'],
                     one['operationAmount']['currency']['name'])
    assert test.prepare_destination(one['to']) == 'Счет **3655'

def test_prepare_date():
    test = operation(one['date'], one['description'], one['from'],
                     one['to'], one['operationAmount']['amount'],
                     one['operationAmount']['currency']['name'])
    assert test.prepare_date(one['date']) == '07.12.2019'

def test___str__():
    test = operation(one['date'], one['description'], one['from'],
                     one['to'], one['operationAmount']['amount'],
                     one['operationAmount']['currency']['name'])
    assert test.__str__()
    test = operation(two['date'], two['description'], two['from'],
                     two['to'], two['operationAmount']['amount'],
                     two['operationAmount']['currency']['name'])
    assert test.prepare_source(two['from']) == ''