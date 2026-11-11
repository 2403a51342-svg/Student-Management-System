"""Student registration module."""

import json
import os

DATA_FILE = "students.json"


def load_students():
    """Return the list of registered students (empty list if none yet)."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)


def register_student(roll_no, name, branch, year, marks):
    """Add a new student. Roll numbers must be unique."""
    students = load_students()
    if any(s["roll_no"] == roll_no for s in students):
        print(f"Roll number {roll_no} is already registered.")
        return False
    students.append(
        {
            "roll_no": roll_no,
            "name": name,
            "branch": branch,
            "year": year,
            "marks": marks,
        }
    )
    save_students(students)
    print(f"Student {name} registered successfully.")
    return True


if __name__ == "__main__":
    roll_no = input("Roll number: ").strip()
    name = input("Name: ").strip()
    branch = input("Branch: ").strip()
    year = int(input("Year: "))
    marks = float(input("Marks (out of 100): "))
    register_student(roll_no, name, branch, year, marks)
