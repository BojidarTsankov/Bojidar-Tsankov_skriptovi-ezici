class Student:
    def __init__(self, name, sex, points):
        self.name = name
        self.sex = sex
        self.points = points

    def formula(self):
        return round(1 + (self.points / 20), 2)


n = int(input("n = "))

students = [
    # Student("Marin", "M", 55),
    # Student("Gergana", "W", 80),
    # Student("Georgi", "M", 100),
    # Student("Mariela", "W", 40),
    # Student("Ralitsa", "W", 60)
]

for i in range(n):
    print(f"Student {i + 1}: ")
    name = str(input("Name: "))
    sex = str(input("Sex (M/W): "))
    points = float(input("Points: "))
    students.append(Student(name, sex, points))

sum_all = 0
for s in students:
    sum_all += s.formula()

average = round(sum_all / n, 2)

sum_m = 0
count_m = 0
for s in students:
    if s.sex == "M":
        sum_m += s.formula()
        count_m += 1

m_avr = round(sum_m / count_m, 2)

sum_w = 0
count_w = 0
for s in students:
    if s.sex == "W":
        sum_w += s.formula()
        count_w += 1

w_avr = round(sum_w / count_w, 2)

print(f"Average is {average}")
print(f"M average is {m_avr}")
print(f"W average is {w_avr}")
