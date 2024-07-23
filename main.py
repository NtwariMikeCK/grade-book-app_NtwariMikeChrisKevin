#!/usr/bin/python3


class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = {}
        self.GPA = 0.0

    def calculate_GPA(self):
        total_credits = sum(course['credits'] for course in self.courses_registered.values())
        total_points = sum(course['grade'] * course['credits'] for course in self.courses_registered.values())
        self.GPA = total_points / total_credits if total_credits > 0 else 0.0

    def register_for_course(self, course, grade):
        self.courses_registered[course.name] = {'credits': course.credits, 'grade': grade}
        self.calculate_GPA()

    def __str__(self):
        return f"{self.names} (Email: {self.email}) - GPA: {self.GPA:.2f}"


class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

    def __str__(self):
        return f"{self.name} - {self.trimester} - {self.credits} credits"


class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)

    def register_student_for_course(self, student_email, course_name, grade):
        student = self.find_student_by_email(student_email)
        course = self.find_course_by_name(course_name)
        if student and course:
            student.register_for_course(course, grade)

    def find_student_by_email(self, email):
        for student in self.student_list:
            if student.email == email:
                return student
        return None

    def find_course_by_name(self, name):
        for course in self.course_list:
            if course.name == name:
                return course
        return None

    def calculate_ranking(self):
        return sorted(self.student_list, key=lambda s: s.GPA, reverse=True)

    def search_by_grade(self, course_name, min_grade, max_grade):
        students = []
        for student in self.student_list:
            if course_name in student.courses_registered:
                if student.courses_registered[course_name]['grade'] >= min_grade and student.courses_registered[course_name]['grade'] <= max_grade:
                  students.append(student)
        return students

    def generate_transcript(self, student_email):
        student = self.find_student_by_email(student_email)
        if student:
            transcript = f"Transcript for {student.names} (Email: {student.email})\n"
            transcript += "Courses:\n"
            for course_name, details in student.courses_registered.items():
                transcript += f"{course_name}: Grade {details['grade']}, Credits {details['credits']}\n"
            transcript += f"GPA: {student.GPA:.2f}\n"
            return transcript
        return "Student not found."


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
