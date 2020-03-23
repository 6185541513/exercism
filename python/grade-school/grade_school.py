class School:
    def __init__(self):
        self.students_by_grade = []  # students_by_grade = List of Objects: Key = Grade. Value = List of Students.

    def add_student(self, name, grade):
        self.students_by_grade.append({name: grade})
        print(self.students_by_grade)

    def roster(self):
        pass

    def grade(self, grade_number):
        pass
