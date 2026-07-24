# grade_report.py

# 1. Student Data Setup
students = [
    {"name": "Alice", "maths": 85, "english": 78, "science": 92},
    {"name": "Bob", "maths": 45, "english": 52, "science": 48},
    {"name": "Charlie", "maths": 95, "english": 88, "science": 91},
    {"name": "Diana", "maths": 62, "english": 70, "science": 68},
    {"name": "Ethan", "maths": 30, "english": 40, "science": 35}
]

# List to store processed student records
results = []

# 2. Main Loop: Process Each Student
for student in students:
    name = student["name"]
    # Calculate average mark across the three subjects
    average = (student["maths"] + student["english"] + student["science"]) / 3
    
    # Grade and Status Logic (Unit 5)
    if average >= 80:
        grade = "A"
        status = "Passed with Distinction"
    elif average >= 70:
        grade = "B"
        status = "Passed"
    elif average >= 60:
        grade = "C"
        status = "Passed"
    elif average >= 50:
        grade = "D"
        status = "Passed"
    else:
        grade = "F"
        status = "Failed"
        
    # Append processed data to results list
    results.append({
        "name": name,
        "average": round(average, 2),
        "grade": grade,
        "status": status
    })

# 3. Class Statistics Calculations
total_averages = [s["average"] for s in results]
class_average = round(sum(total_averages) / len(total_averages), 2)
highest_mark = max(total_averages)
lowest_mark = min(total_averages)

# 4. Display Formatted Class Report
print("=" * 55)
print("             STUDENT GRADE REPORT SUMMARY             ")
print("=" * 55)
print(f"{'Name':<12} | {'Average':<8} | {'Grade':<6} | {'Status'}")
print("-" * 55)

for result in results:
    print(f"{result['name']:<12} | {result['average']:<8.2f} | {result['grade']:<6} | {result['status']}")

print("-" * 55)
print("CLASS STATISTICS:")
print(f"  • Class Average: {class_average}%")
print(f"  • Highest Average: {highest_mark}%")
print(f"  • Lowest Average:  {lowest_mark}%")
print("=" * 55)
print("\n")

# 5. Interactive Student Search (While Loop)
while True:
    search_name = input("Enter student name to search (or type 'exit' to quit): ").strip()
    
    if search_name.lower() == 'exit':
        print("Exiting grade report program. Good luck!")
        break

    found = False
    for s in results:
        if s["name"].lower() == search_name.lower():
            print(f"\n--- Result for {s['name']} ---")
            print(f"Average: {s['average']}%")
            print(f"Grade:   {s['grade']}")
            print(f"Status:  {s['status']}\n")
            found = True
            break
            
    if not found:
        print(f"No student found with the name '{search_name}'. Please try again.\n")