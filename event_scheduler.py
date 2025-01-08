from datetime import datetime

class EventScheduler:
    def __init__(self):
        self.event_scheduler = {}

    def add_event(self, date_time, description):
        try:
            date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
            event_id = 0
            self.event_scheduler[event_id] = {
                "date_time": date_time,
                "description": description
            }
            event_id += 1
            return f"Event added: ID {event_id} - {date_time} - {description}"
        except ValueError:
            return "Invalid date-time format. Please use 'YYYY-MM-DD HH:MM'."

    def sort_by_date(self):

        # Convert dictionary to list of tuples
        event_list = list(self.event_scheduler.items())
        n = len(event_list)

        for i in range(1, n):
            key = event_list[i]
            j = i - 1

            # compare the time of event j  next event(i)
            while j >= 0 and event_list[j][1]['date_time'] > key[1]['date_time']:
                event_list[j + 1] = event_list[j]
                j -= 1
            event_list[j + 1] = key

        return event_list

    def view_events(self):
        if not self.event_scheduler:
            return "No events scheduled."

        events_list = []
        sorted_events = self.sort_by_date()

        # Loop through each event in the sorted list and format the event information
        for event_id, event in sorted_events:
            event_details = f"ID {event_id}: {event['date_time']} - {event['description']}"
            events_list.append(event_details)

        # Join the list of event details into a single string, with each event on a new line
        return "\n".join(events_list)

    # Function to remove an event
    def remove_event(self, event_id):
        if event_id in self.event_scheduler:
            del self.event_scheduler[event_id]
            return f"Event removed: ID {event_id}"
        else:
            return "No event found for that ID."


    def remove_past_events(self):
        current_time = datetime.now()
        events_removed = 0

        for event_id, event in list(self.event_scheduler.items()):
            if event['date_time'] < current_time:
                del self.event_scheduler[event_id]
                events_removed += 1

        if events_removed != 0:
            return "Past events have been removed."
        else:
            return "No past events to remove."

# Just for the command line interface
def CLI():
    scheduler = EventScheduler()

    while True:
        print("\nEvent Scheduler CLI")
        print("1. Add Event")
        print("2. View Events")
        print("3. Remove Event")
        print("4. Remove Past Events")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date_time = input("Enter event date and time (YYYY-MM-DD HH:MM): ")
            description = input("Enter event description: ")
            result = scheduler.add_event(date_time, description)
            print(result)

        elif choice == "2":
            print("\nScheduled Events:")
            print(scheduler.view_events())

        elif choice == "3":
            try:
                event_id = int(input("Enter the event ID to remove: "))
                result = scheduler.remove_event(event_id)
                print(result)
            except ValueError:
                print("Invalid input. Please enter a valid event ID.")

        elif choice == "4":
            result = scheduler.remove_past_events()
            print(result)

        elif choice == "5":
            print("Exiting Event Scheduler. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    CLI()
