from functools import lru_cache
from os import path

from requests import get, post

from flask import Blueprint, current_app, jsonify, render_template

app = Blueprint("character", __name__, url_prefix="/character")

API_ROOT = "https://swapi.co/api/"


def _request_for(api_address):
    return get(api_address).json()


def _convert_url_to_value(item_type, name_in_dict, payload):
    for item in payload:
        if item.get(item_type):
            result = []
            for url in item.get(item_type):
                result.append(_request_for(url)[name_in_dict])

            item[item_type] = result

    return result


@lru_cache(64)
def character_api(number_of_pages=9):
    result = []

    for item in range(1, number_of_pages + 1):
        api_result = get(path.join(API_ROOT, f"people/?page={item}"))

        result = result + api_result.json()["results"]

    # since homeworld is not a list of urls,
    # the _convert_url_to_value function will not be used

    for item in result:
        if item.get("homeworld"):
            home = _request_for(item["homeworld"])

            item["homeworld"] = home["name"]

    _convert_url_to_value("starships", "name", result)
    _convert_url_to_value("vehicles", "name", result)
    _convert_url_to_value("films", "title", result)

    return result


@app.route("/")
def char_index():
    result = character_api()

    return render_template("character.html", chars=result)
