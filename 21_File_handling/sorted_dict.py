data = {"D": 56, "E": 12, "F": 69, "C": 45, "B": 23, "A": 67}

sorted_data = dict(reversed(sorted(data.items(), key=lambda t: t[1])[-3:]))

print(sorted_data)
# for elem in sorted_data: print(elem)