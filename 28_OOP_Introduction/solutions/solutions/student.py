class Student:
    def __init__(self, full_name, group_number, achievements):
        self.full_name = full_name
        self.group_number = group_number
        self.achievements = achievements

    def average_score(self):
        return sum(self.achievements) / len(self.achievements)

    # def __repr__(self):
    #     return "Student(full_name, group_number, achievements)"

    def __str__(self):
        return f"{self.full_name}, Group: {self.group_number}, Average Score: {self.average_score():.2f}"

# Example data for 10 students
students_data = [
    ("Alice Johnson", "A1", [88, 92, 85, 90, 87]),
    ("Bob Smith", "A2", [76, 81, 78, 75, 79]),
    ("Carol White", "A1", [91, 90, 92, 89, 93]),
    ("David Brown", "B1", [68, 72, 70, 69, 71]),
    ("Eve Davis", "B2", [83, 85, 82, 84, 81]),
    ("Frank Miller", "B1", [77, 79, 75, 78, 76]),
    ("Grace Wilson", "A2", [93, 95, 94, 92, 91]),
    ("Henry Taylor", "B2", [81, 80, 79, 82, 83]),
    ("Isabel Adams", "A1", [87, 89, 85, 88, 86]),
    ("Jack Clark", "B1", [73, 75, 74, 72, 70])
]

# Creating a list of students
students = [Student(name, group, scores) for name, group, scores in students_data]

# # Sorting the list by increasing average score
students.sort(key=lambda student: student.average_score())

# # Displaying the sorted list
for student in students:
    print(student)

