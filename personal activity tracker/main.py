import csv
import os
from datetime import datetime

FILE_NAME = "activities.csv"

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Activity", "Duration(min)"])

def add_activity():
    activity = input("Enter activity name: ").strip()
    if not activity:
        print("Activity name cannot be empty.")
        return

    try:
        duration = int(input("Enter duration in minutes: "))
        if duration <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid duration.")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, activity, duration])

    print("✅ Activity added successfully!")

def view_activities():
    if not os.path.exists(FILE_NAME):
        print("No activities found.")
        return

    with open(FILE_NAME, mode="r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if len(rows) <= 1:
        print("No activities logged yet.")
        return

    print("\n📋 Logged Activities:")
    for row in rows[1:]:
        print(f"Date: {row[0]} | Activity: {row[1]} | Duration: {row[2]} min")

def view_summary():
    if not os.path.exists(FILE_NAME):
        print("No data to summarize.")
        return

    total_time = 0
    with open(FILE_NAME, mode="r") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            total_time += int(row[2])

    print(f"\n📊 Total time spent on activities: {total_time} minutes")

def main():
    init_file()
    while True:
        print("\n=== Personal Activity Tracker ===")
        print("1. Add Activity")
        print("2. View Activities")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_activity()
        elif choice == "2":
            view_activities()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
