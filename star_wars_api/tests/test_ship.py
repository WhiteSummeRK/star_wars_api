import unittest
from unittest import mock

from api.ship import ship_api, calculate_score


class TestCharacter(unittest.TestCase):
    def test_calculate_score_should_return_correct_ships(self):
        ships = [
            {
                "cost_in_credits": "unknown",
                "hyperdrive_rating": "unknown"
            },
            {
                "cost_in_credits": "10",
                "hyperdrive_rating": "2"
            },
            {
                "cost_in_credits": "20",
                "hyperdrive_rating": "2"
            }
        ]
        self.assertEqual(calculate_score(ships), [
            {
                "cost_in_credits": "unknown",
                "hyperdrive_rating": "unknown",
                "score": 0
            },
            {
                "cost_in_credits": "10",
                "hyperdrive_rating": "2",
                "score": 5
            },
            {
                "cost_in_credits": "20",
                "hyperdrive_rating": "2",
                "score": 10
            }
        ])
    
    @mock.patch("api.ship.get")
    def test_ship_api_function_should_make_a_lot_of_get_requests(self, mocked_get):
        ship_api(5)

        self.assertEqual(mocked_get.call_count, 5)