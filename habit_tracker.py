# habit_tracker.py

habits = {}

def add_habit(habit):
    habits[habit] = 0

def check_in(habit):
    if habit in habits:
        habits[habit] += 1
    else:
        print("Habit not found.")

def view_habits():
    for habit, streak in habits.items():
        print(f"{habit}: {streak} days")

# Sample usage
add_habit("Exercise")
check_in("Exercise")
view_habits()
