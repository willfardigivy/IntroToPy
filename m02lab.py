last = input("Please print student's last name or ZZZ to quit: ")


while last != "ZZZ":
    first = input("Please print student's first name: ")
    gpa = float(input("Please print student's GPA: "))
    if gpa >= 3.5:
        print(first, last, "made the Dean's List.")
    if gpa >= 3.25:
        print(first, last, "made the Honor Roll.")
    last = input("Please print student's last name or ZZZ to quit: ")
