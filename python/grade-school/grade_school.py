from functools import reduce

class School(object):
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if grade in self.students:
            self.students[grade] = self._add_student(name, self.students[grade])
        else:
            self.students[grade] = [name]  

    def roster(self):
        if self.students:
            return reduce(lambda x, y : x + y, [names for names in self.students.values()])
        else:
            return []    

    def grade(self, grade_number):
        if grade_number in self.students:
            return self.students[grade_number]
        else:
            return []    

    def _add_student(self, name, names):
        for i in range(len(names)):
            if names[i] > name:
               break
        if (i + 1) == len(names) and names[i] < name:
            return names + [name]
        else:
            return (names[:i] + [name] + names[i:])
