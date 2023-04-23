from namefunc import how_many_students_names_start_with_a_letter, print_all_names_one_by_one

name_of_students = ["Kian", "Mohsen", "Emad", "Emam"]

# How many students' name start with E?
counter = 0
for name in name_of_students:
    if name[0] == "E":
        counter += 1

print (counter)

# How many students' name start with M?
counter = 0
for name in name_of_students:
    if name[0] == "M":
        counter += 1

print(counter)
        

print (how_many_students_names_start_with_a_letter(name_of_students, "K"))


print_all_names_one_by_one(name_of_students)