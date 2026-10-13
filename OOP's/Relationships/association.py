'''
Association : two classes are linked and work together,
              but NEITHER owns the other. Both can exist on their own.

Example     : Teacher teaches Student.
              If the teacher is deleted, the student still exists (and vice versa).

UML diagram :

+---------------------------+                 +---------------------+
|          Teacher          |                 |       Student       |
+---------------------------+                 +---------------------+
| - name : str              |    teaches      | - name : str        |
+---------------------------+---------------->+---------------------+
| + get_name() : str        |                 | + get_name() : str  |
| + teach(s: Student): None |                 +---------------------+
+---------------------------+

UML symbols :
    -   private      (self.__name)
    +   public
    #   protected    (self._name)
    ------------    solid line  = association
    ----------->    arrow       = one-way (Teacher knows Student, Student doesn't know Teacher)
    no arrow        = two-way (both know each other)

Multiplicity (how many objects are linked):
    Teacher 1 ------------ * Student      -> one teacher, many students
    1     exactly one
    0..1  zero or one
    *     zero or many
    1..*  at least one
'''


class Teacher:
    def __init__(self, name:str)->None:
        self.__name:str = name #Private

    def get_name(self)->str:
        return self.__name

    def teach(self, studet: "Student") -> None:
         print(f"{self.__name} is teaching {studet.get_name()}")



class Student:
    def __init__(self, name:str)->None:
        self.__name:str = name

    def get_name(self)->str:
        return self.__name



teacher1 = Teacher("Pravin Nalawade")
Student1 = Student("Ganesh")

teacher1.teach(Student1)


'''
Notes:
1. Both objects are created separately (teacher1, Student1).
   Teacher does not create or own Student -> that's why it's association.

2. Here Teacher uses Student only inside teach() and doesn't keep it.
   Strict UML calls this short-term use a "dependency" (dashed arrow - - - ->).
   If Teacher stored the student (e.g. self.students = [...]), it's a full association (solid line).
   Many tutorials call both "association". The main idea is the same: linked, but no ownership.

3. Test: "Can both exist without each other?" -> Yes = association.

4. Real-world examples:
   Doctor  <-> Patient
   Driver  <-> Car
   Customer <-> Bank
'''


'''
Simple rule
Two things work together (teaches, treats, drives) → association
One thing is a group or collection of the other (department, team, library) → aggregation
One thing owns the other, and the part dies with it (house and rooms) → composition

'''