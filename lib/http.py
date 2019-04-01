import json

from django.conf import settings
from django.http import HttpResponse


def render_json(data, code=0):

    json_data = {
        'data': data,
        'code': code,
    }
    if settings.DEBUG:
        result = json.dumps(json_data, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        result = json.dumps(json_data, ensure_ascii=False,separators=[',',':'])

    return HttpResponse(result)
