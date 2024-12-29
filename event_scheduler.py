from datetime import datetime

class EventScheduler:
    def __init__(self):
        self.event_scheduler = {}
        self.event_counter = 1  # To generate unique IDs for events

    # Function to add an event
    def add_event(self, date_time, description):
        try:
            date_time_obj = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
            event_id = self.event_counter
            self.event_scheduler[event_id] = {
                "date_time": date_time_obj,
                "description": description
            }
            self.event_counter += 1
            return f"Event added: ID {event_id} - {date_time_obj} - {description}"
        except ValueError:
            return "Invalid date-time format. Please use 'YYYY-MM-DD HH:MM'."

    # Function to view events
    def view_events(self):
        if not self.event_scheduler:
            return "No events scheduled."
        else:
            events_list = []
            for event_id, event in sorted(self.event_scheduler.items(), key=lambda x: x[1]['date_time']):
                events_list.append(f"ID {event_id}: {event['date_time']} - {event['description']}")
            return "\n".join(events_list)

    # Function to remove an event
    def remove_event(self, event_id):
        if event_id in self.event_scheduler:
            del self.event_scheduler[event_id]
            return f"Event removed: ID {event_id}"
        else:
            return "No event found for that ID."

    # Function to automatically remove events that have ended
    def remove_past_events(self):
        current_time = datetime.now()
        events_to_remove = [event_id for event_id, event in self.event_scheduler.items() if
                            event['date_time'] < current_time]
        removed_events = []
        for event_id in events_to_remove:
            del self.event_scheduler[event_id]
            removed_events.append(f"Event automatically removed: ID {event_id} (Event time has passed)")
        return "\n".join(removed_events) if removed_events else "No past events to remove."






