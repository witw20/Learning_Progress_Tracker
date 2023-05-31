# Learning Progress Tractor of Hyperskill
import re
def main():
    print_menu()

def print_menu() -> None:
    print("Learning progress tracker")
    student_num = 0
    student_dict = dict()
    email_set = set()

    while True:
        choice = input()

        if len(choice.strip()) == 0:
            print("No input")
        elif choice.strip() == "add students":
            add_student()

        elif choice.strip() == "back":
            print("Enter 'exit' to exit the program.")

        elif choice.strip() == "list":
            if len(student_dict) == 0:
                print("No students found")
            else:
                print("Students:")
                for key in student_dict.keys():
                    print(key)

        elif choice.strip() == "add points":
            add_point()

        elif choice.strip() == "find":
            find_student()

        elif choice.strip() == "statistics":
            statistics()



        elif choice.strip() == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command!")


def check_fname(name: str) -> bool:
    if re.match("^[A-Za-z]+[\-']?[A-Za-z]+$", name) and len(name) > 1\
            and name[0] not in ("'", "-")\
            and name[-1] not in ("'", "-"):
        return True
    else:
        return False

def check_lname(name: str) -> bool:
    if re.match("^[A-Za-z]+(?:([ \'-]?[A-Za-z]+)?)*$", name)\
            and len(name) > 1\
            and name[0] not in ("'", "-")\
            and name[-1] not in ("'", "-"):
        return True
    else:
        return False

def check_email(email: str) -> bool:
    if re.match("^[\w\.-]+@[\w\.-]+\.\w+$", email):
        return True
    else:
        return False

def check_point(point_list: list) -> bool:
    for point in point_list:
        if point.isdigit() == False:
            return False
            break
    return True

def add_student() -> None:
    print("Enter student credentials or 'back' to return:")
    while True:
        student_info = input()
        if student_info == "back":
            print(f"Total {student_num} students have been added.")
            break
        elif len(student_info.split()) < 3:
            print("Incorrect credentials.")
            continue

        else:
            try:
                first_name = student_info.split()[0]
                email = student_info.split()[-1]
                last_name = student_info[len(first_name) + 1:-len(email) - 1]
            except Exception:
                print("Incorrect credentials.")
                continue
            else:
                if check_fname(first_name) == False:
                    print("Incorrect first name")
                    continue
                elif check_lname(last_name) == False:
                    print("Incorrect last name")
                    continue
                elif check_email(email) == False:
                    print("Incorrect email")
                    continue
                elif email in email_set:
                    print("This email is already taken.")
                    continue
                else:
                    id_str = str(1000 + student_num)
                    student_dict[id_str] = {"first_name": first_name,
                                            "last_name": last_name,
                                            "email": email,
                                            "python_score": 0,
                                            "DSA_score": 0,
                                            "datebase_score": 0,
                                            "flask_score": 0}
                    email_set.add(email)
                    print("The student has been added.")
                    student_num += 1

def add_point() -> None:
    print("Enter an id and points or 'back' to return:")
    while True:
        student_point = input()
        if student_point == "back":
            break
        elif len(student_point.split()) != 5 \
                or check_point(student_point.split()[1:]) == False:
            print("Incorrect points format.")
            continue
        elif student_point.split()[0] not in student_dict:
            print(f"No student is found for id={student_point.split()[0]}")
            continue
        else:
            student_id = student_point.split()[0]
            student_dict[student_id]["python_score"] += int(student_point.split()[1])
            student_dict[student_id]["DSA_score"] += int(student_point.split()[2])
            student_dict[student_id]["datebase_score"] += int(student_point.split()[3])
            student_dict[student_id]["flask_score"] += int(student_point.split()[4])
            print("Points updated")

def find_student() -> None:
    print("Enter an id or 'back' to return:")
    while True:
        student_id_info = input()
        if student_id_info == "back":
            break
        elif student_id_info not in student_dict:
            print(f"No student is found for id={student_id_info}")
        else:
            print(student_id_info, "points:", \
                  f'Python={student_dict[student_id_info]["python_score"]};', \
                  f'DSA={student_dict[student_id_info]["DSA_score"]};', \
                  f'Databases={student_dict[student_id_info]["datebase_score"]};', \
                  f'Flask={student_dict[student_id_info]["flask_score"]}', sep=" ")

def statistics() -> None:
    print("Type the name of a course to see details or 'back' to quit:")
    course_list = ["Python", "DSA", "Databases", "Flask"]
    # popular
    # activity
    # easiness
    while True:
        course_st = input()
        if course_st == "back":
            break
        elif course_st not in course_list:
            print("Unknown course")
        else:



if __name__ == '__main__':
    main()