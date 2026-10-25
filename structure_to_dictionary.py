from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "course"])

s = Student("Jay", 18, "B.Tech CSE")

d = s._asdict()

print(d)
