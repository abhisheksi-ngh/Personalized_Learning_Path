import json
import os
from datetime import datetime, timedelta

# File paths
attendance_file = os.path.join(os.path.dirname(__file__), "../data/attendance.json")
report_file = os.path.join(os.path.dirname(__file__), "../reports/weekly_reports.json")

def generate_weekly_report():
    # Load attendance data
    try:
        with open(attendance_file, "r") as file:
            attendance_data = json.load(file).get("attendance", [])
    except FileNotFoundError:
        print("No attendance data file found.")
        return

    if not attendance_data:
        print("Attendance data is empty. No report generated.")
        return

    # Calculate one week ago
    one_week_ago = datetime.now() - timedelta(days=7)

    # Filter attendance for the last week
    weekly_attendance = []
    for record in attendance_data:
        try:
            record_date = datetime.strptime(record["date"], "%Y-%m-%d %H:%M:%S")
            if record_date >= one_week_ago:
                weekly_attendance.append(record)
        except ValueError:
            print(f"Invalid date format in record: {record}")
            continue

    # Generate report
    report = {}
    for record in weekly_attendance:
        student_id = record["student_id"]
        workshop_id = record["workshop_id"]
        report[student_id] = report.get(student_id, {})
        report[student_id][workshop_id] = report[student_id].get(workshop_id, 0) + 1

    # Save the report
    try:
        with open(report_file, "w") as file:
            json.dump(report, file, indent=4)
        print(f"Weekly report generated successfully and saved to {report_file}.")
    except IOError as e:
        print(f"Error saving the report: {e}")

# Example usage
if __name__ == "__main__":
    generate_weekly_report()
