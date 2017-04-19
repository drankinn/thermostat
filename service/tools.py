import json
from functools import wraps

import logging
import web

logger = logging.getLogger(__name__)


class MissingValueException(Exception):
    pass


def handle_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = {}
        errors = []
        try:
            raw_data = web.data()
            if raw_data:
                kwargs['data'] = json.loads(raw_data)

            data = func(*args, **kwargs)

        except Exception as ex:
            ex_name = ex.__class__.__name__
            logger.error(ex, exc_info=True)
            errors.append(ex_name + ': ' + str(ex))

        return json.dumps({
            "data": data,
            "errors": errors,
            "success": len(errors) == 0
        })

    return wrapper
