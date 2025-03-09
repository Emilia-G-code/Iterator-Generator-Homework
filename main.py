class Students:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        for value in range(self.start, self.end):
            yield value  

students_in_class = Students(1, 16)

for number in students_in_class:
    print(number)