#!/usr/bin/python3

from student import Student
from course import Course
from gradebook import GradeBook

def main():
    gradebook = GradeBook()

    while True:
        print("\nGrade Book Application")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
            print("Student added successfully.")
        elif choice == "2":
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
            print("Course added successfully.")
        elif choice == "3":
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            gradebook.register_student_for_course(email, course_name, grade)
            print("Student registered for course successfully.")
        elif choice == "4":
            ranking = gradebook.calculate_ranking()
            print("Student Ranking (based on GPA):")
            for rank, student in enumerate(ranking, 1):
                print(f"{rank}. {student}")
        elif choice == "5":
            course_name = input("Enter course name: ")
            min_grade = float(input("Enter minimum grade: "))
            max_grade = float(input("Enter maximum grade: "))
            students = gradebook.search_by_grade(course_name, min_grade, max_grade)
            print(f"Students with grades between {min_grade} and {max_grade} in {course_name}:")
            for student in students:
                print(student)
        elif choice == "6":
            email = input("Enter student email: ")
            transcript = gradebook.generate_transcript(email)
            print(transcript)
        elif choice == "7":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
