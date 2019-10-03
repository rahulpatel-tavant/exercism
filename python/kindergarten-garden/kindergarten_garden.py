class Garden(object):
    def __init__(self, diagram, students = []):
        self.rows = diagram.split("\n")
        self.students = students or ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
        self.students.sort()

    def plants(self, student):
        student_position = self.students.index(student)
        cup_postion = 2 * student_position
        cups = ''.join(row[cup_postion:(2 + cup_postion)] for row in self.rows)
        plants = {'V' : 'Violets', 'G' : 'Grass', 'R' : 'Radishes', 'C' : 'Clover'}
        return [plants[cup] for cup in cups]


