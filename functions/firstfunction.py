def greet_student(name):
   
    print(f"Hello {name}, welcome to the Python class!")


def calculate_total(marks):
   
    return sum(marks)


def calculate_average(total, count):
   
    return total / count


def check_result(average):
   
    if average >= 40:
        return "PASS"
    return "FAIL"


def display_result(name, marks):
    """
    Main function that calls other functions.
    """
    total = calculate_total(marks)
    average = calculate_average(total, len(marks))
    result = check_result(average)

    greet_student(name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Result:", result)


# Program execution starts here
if __name__ == "__main__":
    STUDENT_NAME = "Thriam"
    student_marks = [65, 70, 55, 86, 50]

    display_result(STUDENT_NAME, student_marks)