from datetime import datetime
from tkinter import messagebox

class EventScheduler:
    def __init__(self):
        self.event_scheduler = {}
        self.event_id = 0

    def add_event(self, date_time, description):
        try:
            # Parse the date_time string into a datetime object
            date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
            self.event_scheduler[self.event_id] = {"description": description, "date_time": date_time}
            messagebox.showinfo("Success", f"Event added: ID {self.event_id} - {date_time} - {description}")
            self.event_id += 1  # Increment event_id for the next event
        except ValueError:
            messagebox.showerror("Error", "Field Empty or Invalid date-time format. Please use 'YYYY-MM-DD HH:MM'.")

    def sort_by_date(self):
        event_list = list(self.event_scheduler.items())
        n=len(event_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if event_list[j][1]['date_time'] > event_list[j + 1][1]['date_time']:
                    event_list[j], event_list[j + 1] = event_list[j + 1], event_list[j]
        return event_list

    def view_events(self):
        if not self.event_scheduler:
            return []
        sorted_events = self.sort_by_date()
        formatted_events = []

        for event_id, event in sorted_events:
            description = event['description']
            formatted_date_time = event['date_time'].strftime('%Y-%m-%d %H:%M')
            formatted_events.append((event_id, description, formatted_date_time))

        return formatted_events

    def remove_event(self,event_id):
        if event_id in self.event_scheduler:
            del self.event_scheduler[event_id]
            return True
        else:
            return False


    def remove_past_events(self):
        current_time=datetime.now()
        events_removed = True

        for event_id, event in list(self.event_scheduler.items()):
            if event['date_time']<current_time:
                del self.event_scheduler[event_id]
                events_removed = True

        if events_removed is True:
            return True
        else:
            return False
