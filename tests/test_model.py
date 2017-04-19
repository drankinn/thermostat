import pytest
from voluptuous import MultipleInvalid

from service.models.thermostat import new, schema, edit, view, get_all
from service.db import clear_thermostats


@pytest.fixture(scope='function')
def flush_db():
    clear_thermostats()


def test_new(flush_db):
    doc = {}
    therm = new(doc)
    assert therm == schema(
        {'id': 1, 'name': 'Thermostat 1', 'hot_set_point': 75, 'curr_temp': 60,
         'cool_set_point': 65})

    doc2 = {
        'hot_set_point': 75, 'curr_temp': 60, 'cool_set_point': 65
    }
    therm2 = new(doc2)
    assert therm2 == schema(
        {'id': 2, 'name': 'Thermostat 2', 'hot_set_point': 75, 'curr_temp': 60,
         'cool_set_point': 65})


def test_edit(flush_db):
    # test expected to succeed for a normal edit
    therm = new({})
    therm2 = edit({
        'id': 1,
        'hot_set_point': 65,
        'cool_set_point': 50
    })
    assert therm != therm2
    assert therm2 == schema(
        {'id': 1, 'name': 'Thermostat 1', 'hot_set_point': 65, 'curr_temp': 60,
         'cool_set_point': 50})

    # test ranges on hot and cool set points.  valid between 30 and 100
    with pytest.raises(Exception) as excinfo:
        therm3 = edit({
            'id': 1,
            'hot_set_point': 110,
            'cool_set_point': 22
        })
    assert excinfo.type == MultipleInvalid
    therm3 = view(1)
    # since the edit should have failed,
    # assert that therm2 is still in the same as what's in the db
    assert therm3 == therm2


def test_view(flush_db):
    new({})
    therm2 = view(1)
    assert therm2 == schema(
        {'id': 1, 'name': 'Thermostat 1', 'hot_set_point': 75, 'curr_temp': 60,
         'cool_set_point': 65})
    with pytest.raises(Exception) as excinfo:
        therm3 = view(99)
    assert excinfo.type == Exception


def test_list(flush_db):
    new({})
    new({})
    new({})
    therm_list = get_all()
    assert len(therm_list) == 3
    assert therm_list == {
        1: {'id': 1, 'name': 'Thermostat 1', 'hot_set_point': 75,
            'cool_set_point': 65, 'curr_temp': 60},
        2: {'id': 2, 'name': 'Thermostat 2', 'hot_set_point': 75,
            'cool_set_point': 65, 'curr_temp': 60},
        3: {'id': 3, 'name': 'Thermostat 3', 'hot_set_point': 75,
            'cool_set_point': 65, 'curr_temp': 60}}
