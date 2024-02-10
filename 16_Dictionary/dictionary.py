# empty = {}
# empty = dict()
# print(empty)
# print(type(empty))

# declarate dictionary
# students_grades = {'Yuri': 10, 'Argam': 2}
# students_grades = dict(Yuri=10, Argam=2)
# students_grades = dict([('Yuri', 10), ('Argam', 2)])

# zip object
# students_names = ['Yuri', 'Argam', 'Gagik', 'Hayro']
# students_grades = [10, 2]
# students_grades_dict = dict(zip(students_names, students_grades))
# print(students_grades_dict)
# print(students_grades_dict['Yuri'])


# adding, changing, deleting
# students = {'Yuri': 10, 'Argam': 9}

# students['Gagik'] = 8
# students['Yuri'] = 2
# del students['Yuri']
# print(students)

# dict methods
# students = {'Yuri': 10, 'Argam': 2}

# adding, updateing
# students.setdefault('Gagik', 8)
# students.setdefault('Yuri', 8)
# updated_students_dict = {'Yuri': 2, 'Gagik': 11, 'Hayro': 7}
# students.update(updated_students_dict)

# students_names = ['Yuri', 'Gagik', 'Argam']
# students_dict = dict.fromkeys(students_names, False)
# print(students_dict)

# students = {**students, **updated_students_dict}
# students = students | updated_students_dict
# print(students)

# deleting
# students = {'Yuri': 10, 'Argam': 9}
# del students['Yuri']

# yuri = students.pop('Yuri')
# print(students)
# print(yuri)

# t = students.popitem()
# print(students)
# print(t)

# students.clear()
# print(students)

# get
# students = {'Yuri': 10, 'Argam': 9}
# student = input('Enter student name: ')
# # print(students[student])
# print(students.get(student, 'Unknown student'))
#
# for i in range(10): print(i)

# keys, values, items
# students = {'Yuri': 10, 'Argam': 2}
# keys = list(students.keys())
# values = list(students.values())
# items = list(students.items())
# print(items)


# iterate over dict
# students = {'Yuri': 10, 'Argam': 2}

# for student in students:
#     print(student, '>>', students[student])

# for student in students.keys():
#     print(student, '>>', students[student])

# for value in students.values():
#     print(value)

# for items in students.items():
#     print(items)

# for key, value in students.items():
#     print(key, value)


# copy
# shallow copy
# students = {'Yuri': 10, 'Argam': 2}
# students_copy = students.copy()
# students_copy['Gagik'] = 10
# print(students)
# print(students_copy)

# nested dicts, deep copy
import pprint
import copy

students = {
    'Yuri': {
        'address': 'Komitas Ave.',
        'email': 'Yuri@gmail.com',
        'phone': +37412313231,
        'languages': ['Bash', 'Python', 'C', 'VBA']
    },
    'Argam': {
        'address': 'Hyusisayin Ave.',
        'email': 'Argam@gmail.com',
        'phone': +37412435151,
        'languages': ['Python', 'Java']
    }
}

# pprint.pprint(students)

# students_copy = students.copy()
# students_copy = copy.deepcopy(students)
# students_copy['Yuri']['languages'][0] = 'C++'
# pprint.pprint(students)


# dict comprehensions
# d = {i:i**2 for i in range(1, 10)}
# d = {i:i**2 for i in range(1, 10) if i % 2 == 0}
# pprint.pprint(d)
# for k, v in d.items():
#     print(f"{k}:{v}")

