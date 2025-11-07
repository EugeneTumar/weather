import json
import requests

from ..exceptions import CountryNotFound
from ..settings import urls, settings


def get_global_name(name):

    local_response = requests.get(urls.locals_api, {'q': name, 'appid': settings.api_key})
    local_data = json.loads(local_response.content.decode('utf-8'))

    if len(local_data) == 0:
        raise CountryNotFound()
    
    return local_data[0]['name']