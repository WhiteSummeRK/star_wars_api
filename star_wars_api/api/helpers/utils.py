from os import path
from requests import get, post

import constants


def character_api(page_number):
    api_result = get(f"{constants.CHAR_API}page={page_number}").json()
    
    return api_result["results"]

