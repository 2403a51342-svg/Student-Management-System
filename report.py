"""Student report generation module."""

import json
import os

DATA_FILE = "students.json"


def grade_for(marks):
    if marks >= 90:
        return "A"
    if marks >= 75:
        return "B"
    if marks >= 60:
        return "C"
    if marks >= 40:
        return "D"
    return "F"


def generate_report():
    """Print a report of all registered students."""
    if not os.path.exists(DATA_FILE):
        print("No students registered yet.")
        return

    with open(DATA_FILE, "r") as f:
        students = json.load(f)

    if not students:
        print("No students registered yet.")
        return

    print("=" * 62)
    print("STUDENT REPORT")
    print("=" * 62)
    print(f"{'Roll No':<10}{'Name':<20}{'Branch':<10}{'Year':<6}{'Marks':<8}{'Grade'}")
    print("-" * 62)
    for s in students:
        print(
            f"{s['roll_no']:<10}{s['name']:<20}{s['branch']:<10}"
            f"{s['year']:<6}{s['marks']:<8}{grade_for(s['marks'])}"
        )
    print("-" * 62)

    average = sum(s["marks"] for s in students) / len(students)
    print(f"Total students: {len(students)}")
    print(f"Average marks:  {average:.2f}")


if __name__ == "__main__":
    generate_report()
