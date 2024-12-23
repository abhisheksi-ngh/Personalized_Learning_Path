import json
import os
from datetime import datetime

# File paths
attendance_file = os.path.join(os.path.dirname(__file__), "../data/attendance.json")

def log_attendance(student_id, workshop_id, status="Present"):
    # Load existing attendance data
    try:
        with open(attendance_file, "r") as file:
            attendance_data = json.load(file)
    except FileNotFoundError:
        attendance_data = {"attendance": []}

    # Create new attendance entry
    new_entry = {
        "student_id": int(student_id),
        "workshop_id": int(workshop_id),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": status
    }
    
    # Append new entry
    attendance_data["attendance"].append(new_entry)

    # Save updated attendance data
    try:
        with open(attendance_file, "w") as file:
            json.dump(attendance_data, file, indent=4)
        print(f"Attendance logged for student {student_id} in workshop {workshop_id} with status {status}.")
    except IOError as e:
        print(f"Error saving attendance data: {e}")

# Example usage
if __name__ == "__main__":
    student_id = input("Enter the student ID: ").strip()
    workshop_id = input("Enter the workshop ID: ").strip()

    if not student_id.isdigit() or not workshop_id.isdigit():
        print("Error: Both student ID and workshop ID must be integers.")
    else:
        status = input("Enter status (Present/Absent): ").capitalize()
        if status not in ["Present", "Absent"]:
            print("Error: Status must be either 'Present' or 'Absent'.")
        else:
            log_attendance(student_id, workshop_id, status)
