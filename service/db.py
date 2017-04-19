
# this is the in-memory DB ala mongo style document colletions
thermostats = {}

# keep track of ids
_next_id = 0


def next_id():
    global _next_id
    _next_id += 1
    return _next_id


def get_db():
    global thermostats
    return thermostats


def clear_thermostats():
    global thermostats, _next_id
    thermostats = {}
    _next_id = 0
    return
