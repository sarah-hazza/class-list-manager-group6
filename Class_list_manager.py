# Class List Manager - Group 6
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Nora", "Lama", "Reem", "Lama"]


# ===== Each student adds her function BELOW this line =====
# Written by: Sarah Alarifi (task 1)
# This function counts the total number of students in the class list.
def count_names(names):
    return len(names)

def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    # Written by: Sarah Alarifi (task 1)
    print("Number of names:", count_names(names))


main()
