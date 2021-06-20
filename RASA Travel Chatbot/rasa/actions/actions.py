from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher


class ValidateEventForm(Action):
    def name(self) -> Text:
        return "event_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["event", "ticket", "mail"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]


class ActionSubmitEvent(Action):
    def name(self) -> Text:
        return "action_submit_event"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_event",
                                 event=tracker.get_slot("event"),
                                 ticket=tracker.get_slot("ticket"),
                                 mail=tracker.get_slot("mail"))


class ValidateFlightForm(Action):
    def name(self) -> Text:
        return "flight_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["source_city", "destination_city", "flight_date", "class_num", "adult", "child"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]


class ActionSubmitFlight(Action):
    def name(self) -> Text:
        return "action_submit_flight"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_flight",
                                 source_city=tracker.get_slot("source_city"),
                                 destination_city=tracker.get_slot("destination_city"),
                                 flight_date=tracker.get_slot("flight_date"),
                                 class_num=tracker.get_slot("class_num"),
                                 adult=tracker.get_slot("adult"),
                                 child=tracker.get_slot("child"))


class ValidateOtelForm(Action):
    def name(self) -> Text:
        return "otel_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["city", "start_date", "end_date", "person"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]


class ActionSubmitOtel(Action):
    def name(self) -> Text:
        return "action_submit_otel"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_otel",
                                 city=tracker.get_slot("city"),
                                 start_date=tracker.get_slot("start_date"),
                                 end_date=tracker.get_slot("end_date"),
                                 person=tracker.get_slot("person"))

