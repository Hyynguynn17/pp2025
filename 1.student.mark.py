
students = []     
courses = []       
marks = []        

def input_number_of_students():
    return int(input("Enter number of students: "))


def input_students(n):
    for i in range(n):
        sid, name, dob = input(
            f"Student {i+1} (id name dob): "
        ).split()
        students.append({
            "id": sid,
            "name": name,
            "dob": dob
        })


def input_number_of_courses():
    return int(input("Enter number of courses: "))


def input_courses(m):
    for i in range(m):
        cid, cname = input(
            f"Course {i+1} (id name): "
        ).split()
        courses.append({
            "id": cid,
            "name": cname
        })


def input_marks_for_course():
    course_id = input("Enter course id to input marks: ")

    for s in students:
        score = float(input(
            f"Mark of {s['name']}: "
        ))
        while score < 0 or score > 10:
            score = float(input("Invalid mark, re-enter: "))

        marks.append({
            "student_id": s["id"],
            "course_id": course_id,
            "mark": score
        })


def list_courses():
    print("\n--- Courses ---")
    for c in courses:
        print(c["id"], "-", c["name"])


def list_students():
    print("\n--- Students ---")
    for s in students:
        print(s["id"], s["name"], s["dob"])


def show_marks_of_course():
    course_id = input("Enter course id: ")

    print("\nStudent Name   Mark")
    for m in marks:
        if m["course_id"] == course_id:
            for s in students:
                if s["id"] == m["student_id"]:
                    print(s["name"], " ", m["mark"])



n = input_number_of_students()
input_students(n)

m = input_number_of_courses()
input_courses(m)

list_courses()
input_marks_for_course()

list_students()
show_marks_of_course()

