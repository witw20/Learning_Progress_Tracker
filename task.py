# Learning Progress Tractor of Hyperskill
import re, operator
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
                                            "Python": 0,
                                            "DSA": 0,
                                            "Database": 0,
                                            "Flask": 0}
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
            student_dict[student_id]["Python"] += int(student_point.split()[1])
            student_dict[student_id]["DSA"] += int(student_point.split()[2])
            student_dict[student_id]["Database"] += int(student_point.split()[3])
            student_dict[student_id]["Flask"] += int(student_point.split()[4])
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
                  f'Python={student_dict[student_id_info]["Python"]};', \
                  f'DSA={student_dict[student_id_info]["DSA"]};', \
                  f'Databases={student_dict[student_id_info]["Database"]};', \
                  f'Flask={student_dict[student_id_info]["Flask"]}', sep=" ")

def statistics() -> None:
    print("Type the name of a course to see details or 'back' to quit:")
    course_name = ["Python", "DSA", "Databases", "Flask"]
    try:
        python_list = [student_dict[x]["Python"] for x in student_dict]
        dsa_list = [student_dict[x]["DSA"] for x in student_dict]
        db_list = [student_dict[x]["Database"] for x in student_dict]
        flask_list = [student_dict[x]["Flask"] for x in student_dict]
    except Exception:
        print("Most popular: n//a\n\
                Least popular: n//a\n\
                Highest activity: n//a\n\
                Lowest activity: n//a\n\
                Easiest course: n//a\n\
                Hardest course: n//a\n\")
    else:
        if sum(python_list + dsa_list + db_list + flask_list) == 0:
            print("Most popular: n//a\n\
                    Least popular: n//a\n\
                    Highest activity: n//a\n\
                    Lowest activity: n//a\n\
                    Easiest course: n//a\n\
                    Hardest course: n//a\n\")
        else:
            popular()
            activity()
            easy()

    while True:
        course_input = input()
        if course_input == "back":
            break
        elif course_input not in course_list:
            top_student(course_input)
        else:
            print("Unknown course")

def popular() -> None:
    pop_score = list()

    for lst in [python_list, dsa_list, db_list, flask_list]:
        pop_score.append(len([x for x in lst if x > 0]))
    print("Most popular: ", end="")
    for course in course_name:
        print(course_name[i] if pop_score[i] == max(pop_score), sep=" ")
    print("Least popular: ", end="")
    for course in course_name:
        if min(pop_score) < max(pop_score):
            print(course_name[i] if pop_score[i] == min(pop_score), sep=" ")
        else: print("n//a")
    return None

def activity() -> None:
    act_score = list()

    for lst in [python_list, dsa_list, db_list, flask_list]:
        act_score.append(sum([lst]))
    print("Highest activity: ", end="")
    for course in course_name:
        print(course_name[i] if act_score[i] == max(act_score), sep=" ")
    print("Lowest activity: ", end="")
    for course in course_name:
        if min(act_score) < max(act_score):
            print(course_name[i] if act_score[i] == min(act_score), sep=" ")
        else: print("n//a")
    return None

def easy() -> None:
    easy_score = list()

    for lst in [python_list, dsa_list, db_list, flask_list]:
        easy_score.append(sum([lst]) / len([lst]))
    print("Easiest course: ", end="")
    for course in course_name:
        print(course_name[i] if easy_score[i] == max(easy_score), sep=" ")
    print("Hardest course: ", end="")
    for course in course_name:
        if min(easy_score) < max(act_score):
            print(course_name[i] if easy_score[i] == min(easy_score), sep=" ")
        else: print("n//a")
    return None

def top_student(course_input: str) -> None:
    print(course_input)
    print("id    points    completed")
    cmplt_point = {"Python": 600, "DSA": 400, "Database": 480, "Flask": 550}
    stdt_score = {stdt_id: student_dict[stdt_id][course_input]
                    for stdt_id in student_dict
                    if student_dict[stdt_id][course_input] > 0}
    if bool(stdt_score):
        sorted_score = dict(sorted(stdt_score.items(),
                        key=operator.itemgetter(1), reverse=True))
        for k in sorted_score.keys():
            cmplt = sorted_score[k] / cmplt_point[course_input] * 100
            print(f"{k}  {sorted_score[k]}        {round(cmplt, 1)}%")
    return None

if __name__ == '__main__':
    main()
