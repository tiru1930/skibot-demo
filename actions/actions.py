# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGetSchedules(Action):

    def name(self) -> Text:
        return "action_get_schedules"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        schedule_dict = {
            "406-555-1212": ["John  Dec 12 at 9am", "Bob Dec 15 at 1pm"]
        }
        phone_number = tracker.get_slot("phone_number")
        msg_params = {
            "schedules": schedule_dict.get(phone_number),
            "phone_number": phone_number,
            "number": len(schedule_dict.get(phone_number))
        }
        dispatcher.utter_message(response="utter_reschedule_message", **msg_params)

        return []


class ActionGetScheduleDetails(Action):

    def name(self) -> Text:
        return "action_get_schedule_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_messages = []
        for event in tracker.events:
            if (event.get("event") == "user") and (event.get("event") is not None):
                text = event.get("text")
                user_messages.append(text)
        text = user_messages[-1]
        schedule_details = {
            "John  Dec 12 at 9am": ["Private Tuesday Morning from 10-11:45 AM",
                                    "Private Tuesday Afternoon from 1:00 to 2:45 PM",
                                    "Semi-Private Tuesday Morning from 10-12"]
        }
        name = tracker.get_slot("name")
        date = tracker.get_slot("date")
        print(name)
        print(date)
        msg_params = {
            "details": schedule_details.get(text),
            "name": name,
            "date": date
        }
        dispatcher.utter_message(response="utter_schedule_details", **msg_params)

        return []
