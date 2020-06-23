# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

import json
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher

import constants
import utils

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionProductSearch(Action):

    def name(self) -> Text:
        return "action_product_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product_type = tracker.slots['product_type']
        user_type = tracker.slots['user_type']
        color_type = tracker.slots['color_type'] if tracker.slots['color_type'] else ''
        print('product_type: {} || user_type: {} || color_type: {}'.format(
            product_type, user_type, color_type))
        print('##################')
        data = {
                'product_type': product_type,
                'user_type': user_type,
                'query': (color_type + ' ' + product_type + ' ' + user_type).strip()
                }
        product_search_obj = utils.ProductSearchAPI(constants.PRODUCT_SEARCH_API_ENDPOINT, json.dumps(data))
        response = product_search_obj.call_product_search_api()
        dispatcher.utter_message(text=response)
        return [AllSlotsReset()]
