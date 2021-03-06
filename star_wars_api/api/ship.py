from functools import lru_cache
from os import path

from requests import get, post

from flask import Blueprint, current_app, jsonify, render_template

app = Blueprint("ships", __name__, url_prefix="/ships")

API_ROOT = "https://swapi.co/api/"

@lru_cache(64)
def ship_api(number_of_pages=4):
    result = []
    for item in range(1, number_of_pages + 1):
        api_result = get(path.join(API_ROOT, f"starships/?page={item}"))

        result = result + api_result.json()["results"]

    return result


def calculate_score(ships):
    for item in ships:
        if (
            item["cost_in_credits"] != "unknown"
            and item["hyperdrive_rating"] != "unknown"
        ):
            item["score"] = int(item["cost_in_credits"]) // float(
                item["hyperdrive_rating"]
            )
        else:
            item["score"] = 0

    return ships


@app.route("/")
def ship_index():
    ships = ship_api()

    result = calculate_score(ships)

    return render_template("ships.html", ships=result)
