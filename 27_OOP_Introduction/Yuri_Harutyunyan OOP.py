'''ex. 2 - students''' 
class Student:
    def __init__(self, name_surname: str, group_num: int, performance: list) -> None:
        self.name_surname = name_surname
        self.group_num = group_num
        self.performance = performance
    def perf_average(self):
        'Returns average of performance list'
        return sum(self.performance) / len(self.performance)

# student_list = [
#     ['Anna Abrahamyan', 1, [1,5,4,0,3]],
#     ['Abraham Hovakimyan', 1, [5,5,4,5,3]],
#     ['Yuri Harutyunyan', 2, [4,4,5,3,2]],
#     ['Davit Abrahamyan', 2, [1,0,0,4,0]],
#     ['Lilit Sargsyan', 1, [0,1,5,5,4]],
#     ['Kima Petrosyan', 2, [2,3,3,4,2]],
#     ['Stepan Stepanyan', 1, [5,5,5,5,4]],
#     ['Inga Arshakyan', 2, [5,4,1,3,5]],
#     ['Tatul Avoyan', 1, [0,0,0,0,1]],
#     ['Armen Yeritsyan', 1, [1,1,2,5,3]]
# ]

# # Verevi listi elementner@ student class enq sarqum u lcnum enq listi mej
# student_list_class = [Student(val[0], val[1], val[2]) for val in student_list]

# # Nor list enq stanum vortex sort a arvac yst performance-i mijini
# sortedlist = sorted(student_list_class, key = lambda x: x.perf_average(), reverse = True)

# for val in sortedlist:
#     print(f'Name: {val.name_surname}, Average performance: {val.perf_average()}')
# # Stepan Stepanyan@ dasarani gerazancikn a parzvvuma :D
# # Tatul Avoyanin heracnel hamalsaranic!!!!!!!!!


'''ex. 3 - yntaniq'''
class FatherMother:
    def __init__(self, name, age, baby_quantity) -> None:
        self.name = name
        self.age = age
        self.baby_quantity = baby_quantity
    def tell_info(self):
        pass
    def calm_baby(self):
        pass
    def feed_baby(self):
        pass

class Baby:
    def __init__(self, name, age, calm_state, hunger_state) -> None:
        self.name = name
        self.age = age
        self.calm_state = calm_state
        self.hunger_state = hunger_state



'''ex. 4 - magiya'''
class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return Vochmiban()
            
    def answer(self):
        return self.__class__.__name__


class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        else:
            return Vochmiban()

    def answer(self):
        return self.__class__.__name__


class Air:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Water):
            return Storm()
        else:
            return Vochmiban()

    def answer(self):
        return self.__class__.__name__


class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return Vochmiban()

    def answer(self):
        return self.__class__.__name__


class Storm:
    def answer(self):
        return self.__class__.__name__

class Steam:
    def answer(self):
        return self.__class__.__name__

class Dirt:
    def answer(self):
        return self.__class__.__name__

class Dust:
    def answer(self):
        return self.__class__.__name__

class Lightning:
    def answer(self):
        return self.__class__.__name__

class Lava:
    def answer(self):
        return self.__class__.__name__

class Vochmiban:
    def answer(self):
        return 'None'


element1 = Air()
element2 = Lava()
result = element1 + element2
print(result.answer())