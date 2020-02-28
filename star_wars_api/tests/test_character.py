import unittest
from unittest import mock

from api.character import _convert_url_to_value, character_api


class TestCharacter(unittest.TestCase):
    @mock.patch("api.character._request_for")
    def test_convert_url_function_should_make_a_request(self, mocked_func):

        item_type = "item_type"
        name_in_dict = "name"
        payload = [{"item_type": ["url_01", "url_02"]}]

        mocked_func.return_value = {name_in_dict: "return value of function"}

        result = _convert_url_to_value(item_type, name_in_dict, payload)

        self.assertEqual(
            result, ["return value of function", "return value of function"]
        )
        mocked_func.assert_called()

    @mock.patch("api.character._request_for")
    @mock.patch("api.character.get")
    @mock.patch("api.character._convert_url_to_value")
    def test_character_api_should_call_convert_url_tree_times(
        self, mock_convert, mock_get, mock_req
    ):
        number_of_pages = 5

        character_api(number_of_pages)

        self.assertEqual(mock_convert.call_count, 3)
        self.assertEqual(mock_get.call_count, 5)
        self.assertEqual(mock_req.called, False)
