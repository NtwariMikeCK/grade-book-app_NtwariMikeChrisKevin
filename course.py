#!/usr/bin/python3

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

    def __str__(self):
        return f"{self.name} - {self.trimester} - {self.credits} credits"
