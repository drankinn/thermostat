from voluptuous import Schema, REMOVE_EXTRA, Required, All, Range, Length
from service.db import get_db, next_id

FAN_MODE_OFF = 0
FAN_MODE_ON = 1


def edit(data):
    db = get_db()
    if 'id' not in data or data.get('id', -1) not in db:
        raise Exception('thermometer with id {} not found.  '
                        'update failed.'
                        .format(data.get('id', -1)))
    else:
        # get a copy of the record from the db and apply the updates
        thermostat = db[data['id']].copy()
        thermostat.update(data)

        # validate the data after the updates on the copy
        data = clean_and_validate(thermostat)

        # if valid, replace the record with the updates
        db[data['id']] = data
    return data


def new(data):
    db = get_db()
    if data is None:
        data = {}
    data = clean_and_validate(data)
    db[data['id']] = data
    return data


def view(therm_id):
    db = get_db()
    data = db.get(int(therm_id))
    if data is None:
        raise Exception('Thermometer with id {} not found.'
                        .format(therm_id))
    return data


def delete(therm_id):
    db = get_db()
    del db[int(therm_id)]
    return {}

def get_all():
    db = get_db()
    return db.copy()


def clean_and_validate(data):
    if 'id' not in data:
        data['id'] = next_id()
    if 'name' not in data:
        data['name'] = 'Thermostat {}'.format(data['id'])
    if 'fan_mode' in data:
        if data['fan_mode'] == 'ON':
            data['fan_mode'] = FAN_MODE_ON
        else:
            data['fan_mode'] = FAN_MODE_OFF
    data = schema(data)
    return data


schema = Schema({
    Required('id'): All(int, Range(min=0)),
    Required('name'): All(str, Length(min=0)),
    Required('curr_temp', default=60): All(int, Range(min=0)),
    Required('cool_set_point', default=65): All(int, Range(min=30, max=100)),
    Required('hot_set_point', default=75): All(int, Range(min=30, max=100))

}, extra=REMOVE_EXTRA)

