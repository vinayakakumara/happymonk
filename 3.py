class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = []

    def add_course(self, course):
        self.enrolled_courses.append(course)

    def remove_course(self, course):
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)

    def get_course_list(self):
        return [course.title for course in self.enrolled_courses]

class Course:
    def __init__(self, course_code, title, instructor, max_capacity):
        self.course_code = course_code
        self.title = title
        self.instructor = instructor
        self.max_capacity = max_capacity
        self.enrolled_students = []

    def enroll_student(self, student):
        if not self.is_full() and student not in self.enrolled_students:
            self.enrolled_students.append(student)

    def unenroll_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)

    def get_student_list(self):
        return [student.name for student in self.enrolled_students]

    def is_full(self):
        return len(self.enrolled_students) >= self.max_capacity

class University:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
# Create students
student1 = Student(1, "Alice")
student2 = Student(2, "Bob")

# Create courses
course1 = Course("CS101", "Introduction to Programming", "Prof. Smith", 30)
course2 = Course("MATH202", "Calculus II", "Prof. Johnson", 25)

# Create a university
university = University()

# Add students to the university
university.add_student(student1)
university.add_student(student2)

# Add courses to the university
university.add_course(course1)
university.add_course(course2)

# Enroll students in courses
course1.enroll_student(student1)
course1.enroll_student(student2)
course2.enroll_student(student1)

# Get enrolled courses for a student
print(student1.get_course_list())  # Should print ['Introduction to Programming', 'Calculus II']

# Get students enrolled in a course
print(course1.get_student_list())  # Should print ['Alice', 'Bob']
