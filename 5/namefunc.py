def print_all_names_one_by_one(list_1:list[str]) -> None:
    for name in list_1:
        print (name)
        
        
def how_many_students_names_start_with_a_letter(list_1:list[str], letter:str) -> int:
    counter = 0
    for name in list_1:
        if name[0] == letter:
            counter += 1
    return counter

if __name__ == "__main__":
    print("Hey Teddy!")

Khers = "Teddy"