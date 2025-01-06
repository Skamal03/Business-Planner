from datetime import datetime

class EventScheduler:
    def __init__(self):
        self.event_scheduler = {}
        self.unique_ids = 1

    def add_event(self, date_time, description):
        try:
            date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
            event_id = self.unique_ids
            self.event_scheduler[event_id] = {
                "date_time": date_time,
                "description": description
            }
            self.unique_ids += 1
            return f"Event added: ID {event_id} - {date_time} - {description}"
        except ValueError:
            return "Invalid date-time format. Please use 'YYYY-MM-DD HH:MM'."

    def sort_events_by_date(self):

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

        # Step 1: Sort the events using a separate function (manual sort)
        sorted_events = self.sort_events_by_date()

        # Step 2: Loop through each event in the sorted list and format the event information
        for event_id, event in sorted_events:
            event_details = f"ID {event_id}: {event['date_time']} - {event['description']}"
            events_list.append(event_details)

        # Step 3: Join the list of event details into a single string, with each event on a new line
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
        events_to_remove = [event_id for event_id, event in self.event_scheduler.items() if
                            event['date_time'] < current_time]
        removed_events = []
        for event_id in events_to_remove:
            del self.event_scheduler[event_id]
            removed_events.append(f"Event automatically removed: ID {event_id} (Event time has passed)")
        return "\n".join(removed_events) if removed_events else "No past events to remove."


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
