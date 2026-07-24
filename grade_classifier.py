# grade_classifier.py

def main():
    print("=" * 45)
    print("       STUDENT GRADE CLASSIFIER SYSTEM       ")
    print("=" * 45)

    # 1. Collect inputs
    student_name = input("Enter learner's name: ").strip().title()

    # Get marks for three subjects
    mark1 = float(input("Enter mark for Subject 1: ").strip())
    mark2 = float(input("Enter mark for Subject 2: ").strip())
    mark3 = float(input("Enter mark for Subject 3: ").strip())

    # 2. Calculate average mark
    average = (mark1 + mark2 + mark3) / 3

    # 3. Assign letter grade using if/elif/else
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # 4. Assign Pass/Fail status
    if average >= 50:
        status = "PASS"
    else:
        status = "FAIL"

    # 5. Check individual subjects for intervention (< 40)
    flags = []
    if mark1 < 40:
        flags.append("Subject 1")
    if mark2 < 40:
        flags.append("Subject 2")
    if mark3 < 40:
        flags.append("Subject 3")

    # 6. Display Formatted Report Card
    print("\n" + "=" * 45)
    print(f"            REPORT CARD: {student_name.upper()}")
    print("=" * 45)
    print(f"Subject 1 Mark : {mark1:.2f}%")
    print(f"Subject 2 Mark : {mark2:.2f}%")
    print(f"Subject 3 Mark : {mark3:.2f}%")
    print("-" * 45)
    print(f"Average Mark   : {average:.2f}%")
    print(f"Overall Grade  : {grade}")
    print(f"Final Status   : {status}")
    print("-" * 45)

    # Display intervention flags if any subject is under 40%
    if flags:
        print(f"ATTENTION: Needs intervention in {', '.join(flags)} (< 40%)")
    else:
        print("Intervention   : None required (All subjects >= 40%)")

    print("=" * 45)


if __name__ == "__main__":
    main()