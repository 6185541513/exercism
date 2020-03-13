import re


class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.splitlines()
        self.students = students or original_gangsters
        self.students.sort()

    def plants(self, student):
        plant_letters = []
        for i in range(len(self.students)):
            if student == self.students[i]:
                print(f'{student} {i}:{i+1}')
                for pll in self.diagram:
                    plant_letters.append(pll[i*2])
                    plant_letters.append(pll[i*2+1])

        result = []
        print(str(plant_letters))
        for pl in plant_letters:
            for p in plants:
                if pl == p[0]:
                    result.append(p)
        return result


original_gangsters = list(filter(None, re.split(r',|and|\.?\s+', """Alice, Bob, Charlie, David,
Eve, Fred, Ginny, Harriet,
Ileana, Joseph, Kincaid, and Larry.
        """)))  # took longer and is ugly but at least... hmm

plants = list(filter(None, re.split(r',|\s|And', """grass, clover, radishes, and violets""".title())))  # why
