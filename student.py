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
