from flask import current_app, Blueprint, render_template, jsonify
from requests import get, post

from os import path
from helpers import constants

from functools import lru_cache


app = Blueprint('character', __name__, url_prefix='/character')

def _request_for(api_address):
    return get(api_address).json()


@lru_cache(64)
def character_api(number_of_pages=9):
    result = []

    for item in range(1, number_of_pages+1):
        api_result = get(path.join(constants.API_ROOT, f"people/?page={item}"))

        result = result + api_result.json()["results"]

    for item in result:
        if item.get("homeworld"):
            home = _request_for(item["homeworld"])

            item["homeworld"] = home["name"]
    
    for item in result:
        if item.get("starships"):
            starships = []
            for star in item.get("starships"):    
                starships.append(_request_for(star)["name"])


            item["starships"] = starships

    for item in result:
        if item.get("vehicles"):
            vehicles = []
            for veh in item.get("vehicles"):    
                vehicles.append(_request_for(veh)["name"])
    
            item["vehicles"] = vehicles

    for item in result:
        if item.get("films"):
            films = []
            for fil in item.get("films"):    
                films.append(_request_for(fil)["title"])
    
            item["films"] = films

    return result


@app.route('/')
def char_index():
    result = character_api()

    return render_template(
        "character.html",
        chars=result
    )
