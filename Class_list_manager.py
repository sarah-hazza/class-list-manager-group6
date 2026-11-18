# Class List Manager - Group 6
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal","Lama"]


# ===== Each student adds her function BELOW this line =====
# Written by: Sarah Alarifi (task 1)
# This function counts the total number of students in the class list.
def count_names(names):
    return len(names)
# Written by: Aljawharah aljubair (task 2)
# This function searches for a student name.
def search_name(names, name):
    for student in names:
        if student.lower() == name.lower():
            return True
    return False
def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    # Written by: Sarah Alarifi (task 1)
    print("Number of names:", count_names(names))
    # Written by: Aljawharah aljubair (task 2)
    # Found: the name exists in the list
    print("Search for Sara:", search_name(names, "Sara"))
    # Not found: the name is not in the list
    print("Search for Hessa:", search_name(names, "Hessa"))
    # Not case sensitive: lowercase still matches
    print("Search for sara:", search_name(names, "sara"))




main()
