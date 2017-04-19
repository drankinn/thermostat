import logging
from service.models.thermostat import edit, new, get_all, view, delete
from service.tools import handle_json, MissingValueException

logger = logging.getLogger(__name__)


class New(object):
    @handle_json
    def POST(self, data=None):
        return new(data)


class List(object):
    @handle_json
    def GET(self):
        return get_all()


class Edit(object):
    @handle_json
    def POST(self, data=None):
        return edit(data)


class View(object):
    @handle_json
    def GET(self, id):
        if id is None:
            raise MissingValueException('missing required path paremeter id'
                                        ' in /view/{id}')
        return view(id)


class Delete(object):
    @handle_json
    def GET(self, id):
        if id is None:
            raise MissingValueException('missing required path paremeter id'
                                        ' in /delete/{id}')
        return delete(id)