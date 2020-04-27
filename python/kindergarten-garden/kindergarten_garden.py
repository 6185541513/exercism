import re


class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.splitlines()
        self.students = sorted(students or original_gang)

    def plants(self, student):
        seed_index = self.students.index(student)*2
        plant_titles = ''.join(map(lambda plant_row: plant_row[seed_index:seed_index+2], self.diagram))
        return [''.join(list(filter(lambda plant: title == plant[0], plants))) for title in plant_titles]


original_gang = list(filter(None, re.split(r',|and|\.?\s+', """Alice, Bob, Charlie, David,
Eve, Fred, Ginny, Harriet,
Ileana, Joseph, Kincaid, and Larry.
        """)))  # took longer and is ugly but at least... hmm

plants = list(filter(None, re.split(r',|\s|And', """grass, clover, radishes, and violets""".title())))  # why
