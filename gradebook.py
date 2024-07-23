#!/usr/bin/python3

from student import Student
from course import Course



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
