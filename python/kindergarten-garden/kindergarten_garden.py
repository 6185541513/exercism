import re


class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.splitlines()
        self.students = students or original_gangsters
        self.students.sort()

    def plants(self, student):
        student_index = self.students.index(student)
        print(f'{student}:{student_index}')
        plant_letters = ''.join(map(lambda plant_row: plant_row[student_index*2:student_index*2+2], self.diagram))
        print(f'{self.diagram}')
        print(f'{plant_letters}:{student}')
        student_plants = [(plant_name for plant_name in plants if letter == plant_name[0]) for letter in plant_letters]
        print(f'{student_plants}')
        next()


        plant_letters = []
        for i in range(len(self.students)):
            if student == self.students[i]:
                for pll in self.diagram:
                    plant_letters.append(pll[i*2])
                    plant_letters.append(pll[i*2+1])

        result = []
        for pl in plant_letters:
            for p in plants:
                if pl == p[0]:
                    result.append(p)
        return result


original_gangsters = list(filter(None, re.split(r',|and|\.?\s+', """Alice, Bob, Charlie, David,
Eve, Fred, Ginny, Harriet,
Ileana, Joseph, Kincaid, and Larry.
        """)))  # took longer and is ugly but at least... hmm

plants = set(filter(None, re.split(r',|\s|And', """grass, clover, radishes, and violets""".title())))  # why
