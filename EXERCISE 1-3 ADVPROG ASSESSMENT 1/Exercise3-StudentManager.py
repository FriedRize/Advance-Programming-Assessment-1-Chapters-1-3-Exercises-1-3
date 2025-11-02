import os

# ============================
# Utility Functions
# ============================
def load_data(filename):
    students = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            n = int(f.readline().strip())
            for line in f:
                if not line.strip():
                    continue
                parts = [p.strip() for p in line.split(',')]
                if len(parts) < 6:
                    continue
                code = parts[0]
                name = parts[1]
                c1, c2, c3, exam = map(int, parts[2:])
                students.append({
                    'code': code,
                    'name': name,
                    'coursework': [c1, c2, c3],
                    'exam': exam
                })
    except FileNotFoundError:
        print("File not found.")
    return students


def calc_totals(students):
    for s in students:
        total_cw = sum(s['coursework'])
        overall = ((total_cw + s['exam']) / 160) * 100
        s['total_cw'] = total_cw
        s['overall'] = overall
        s['grade'] = assign_grade(overall)
    return students


def assign_grade(pct):
    if pct >= 70:
        return 'A'
    elif pct >= 60:
        return 'B'
    elif pct >= 50:
        return 'C'
    elif pct >= 40:
        return 'D'
    else:
        return 'F'


def display_student(s):
    print(f"\nName: {s['name']}")
    print(f"Student Number: {s['code']}")
    print(f"Coursework Total: {s['total_cw']} / 60")
    print(f"Exam Mark: {s['exam']} / 100")
    print(f"Overall %: {s['overall']:.2f}%")
    print(f"Grade: {s['grade']}")
    print("-" * 35)


# ============================
# Menu Functions
# ============================
def view_all(students):
    print("\n=== All Student Records ===")
    total_pct = 0
    for s in students:
        display_student(s)
        total_pct += s['overall']
    avg = total_pct / len(students) if students else 0
    print(f"\nNumber of students: {len(students)}")
    print(f"Average percentage: {avg:.2f}%\n")


def view_individual(students):
    print("\nSelect a student:")
    for i, s in enumerate(students, 1):
        print(f"{i}. {s['name']}")
    try:
        choice = int(input("Enter number or 0 to cancel: "))
        if choice == 0:
            return
        student = students[choice - 1]
        display_student(student)
    except (ValueError, IndexError):
        print("Invalid selection.")


def show_highest(students):
    if not students:
        print("No data.")
        return
    best = max(students, key=lambda s: s['overall'])
    print("\n=== Highest Total Score ===")
    display_student(best)


def show_lowest(students):
    if not students:
        print("No data.")
        return
    worst = min(students, key=lambda s: s['overall'])
    print("\n=== Lowest Total Score ===")
    display_student(worst)


# ============================
# Main Menu
# ============================
def main():
    filename = 'studentMarks.txt'
    if not os.path.exists(filename):
        print("studentMarks.txt not found.")
        return

    students = load_data(filename)
    students = calc_totals(students)

    while True:
        print("\nSTUDENT MARKS ANALYSIS MENU")
        print("1. View all student records")
        print("2. View individual student record")
        print("3. Show student with highest total score")
        print("4. Show student with lowest total score")
        print("5. Exit")

        choice = input("Enter option (1-5): ").strip()

        if choice == '1':
            view_all(students)
        elif choice == '2':
            view_individual(students)
        elif choice == '3':
            show_highest(students)
        elif choice == '4':
            show_lowest(students)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
