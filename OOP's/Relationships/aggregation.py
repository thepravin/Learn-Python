'''
Aggregation : a weak "HAS-A" relationship.
              One class (whole) holds other objects (parts),
              but the parts are created OUTSIDE and can live on their own.

Example     : Department has Students.
              Students are created first, then added to the department.
              If the department is deleted, the students still exist.

UML diagram : (empty diamond ◇ on the owner/whole side)

+-------------------------------+                 +-------------------------+
|          Department           |                 |         Studet          |
+-------------------------------+ 1             * +-------------------------+
| - dept_name : str             |◇----------------| - name : str            |
| - student : List[Studet]      |                 | - roll_no : int         |
+-------------------------------+                 +-------------------------+
| + add_student(s: Studet)      |                 | + get_name() : str      |
| + show_students() : None      |                 | + get_roll_no() : int   |
+-------------------------------+                 +-------------------------+

Read it as : one Department has many (*) Students.
    ◇   empty diamond = aggregation (sits on the Department side)
    1   exactly one department
    *   zero or many students
'''

from typing import List


# Student class (can exist independently)
class Studet:
    def __init__(self, name:str, roll_no:int)->None:
        self.__name = name
        self.__roll_no=roll_no

    def get_name(self)->str:
        return self.__name

    def get_roll_no(self)->int:
        return self.__roll_no



# Department (Cotains studets - Aggregation)
class Department:
    def __init__(self, dept_name:str)->None:
        self.__dept_name = dept_name
        self.__student:List[Studet] = []

    def add_student(self, student:Studet)->None:
        self.__student.append(student)


    def show_students(self)->None:
        print(f"\nStudents in {self.__dept_name} Department : ")
        for student in self.__student:
            print(f" - {student.get_name()} (Roll No: {student.get_roll_no()})")


# student obj exist independently
s1 = Studet("Pravin", 1)
s2 = Studet("Ganesh",2)
s3 = Studet("Om",3)

# department obj
cs_dept = Department("Computer Science")

cs_dept.add_student(s1)
cs_dept.add_student(s2)
cs_dept.show_students()

del cs_dept

print(s1.get_name()) # work or exist after deleting department
# print(cs_dep.add_studnt())  dosen't work


'''
Notes:
1. Students (s1, s2, s3) are created OUTSIDE the Department and passed in with add_student().
   Department only keeps a reference (link) to them, it does not create them.

2. del cs_dept deletes the department, but s1 still works -> parts live without the whole.

3. One student can be added to more than one department (shared part).
   e.g. ai_dept.add_student(s1) -> s1 is in both departments.

4. Test: "Does it HAS-A, and can the part live without the whole?" -> Yes = aggregation.

5. Aggregation vs association:
   Association -> two classes just work together (Teacher teaches Student), no "has-a".
   Aggregation -> one class holds/collects the others (Department has Students).

6. Real-world examples:
   Department ◇- Students
   Team       ◇- Players
   Library    ◇- Books
   Playlist   ◇- Songs
'''