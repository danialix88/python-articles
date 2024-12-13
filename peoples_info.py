def get_person_info():
    """Gets a person's name, weight, and height from the user.

    Returns:
        A list containing the name, weight, and height.
    """

    name = input("Enter person's name: ")
    weight = int(input("Enter person's weight (kg): "))
    height = float(input("Enter person's height (m): "))

    return [name, weight, height]

def add_person(people_list, person_info):
    """Adds a person to the list, checking for duplicates.

    Args:
        people_list: A list of people.
        person_info: A list containing the name, weight, and height of the person to add.

    Returns:
        The updated list of people.
    """    

    name, _, _ = person_info

    for i, person in enumerate(people_list):
        if person[0] == name:
            overwrite = input(f"Person with name '{name}' already exists. Overwrite? (y/n): ")
            if overwrite.lower() == 'y':
                people_list[i] = person_info
                print(f"Person '{name}' overwritten.")
                return people_list
            else:
                print("Person not added.")
                return people_list

    people_list.append(person_info)
    print(f"Person '{name}' added.")
    return people_list

def remove_person(people_list):
    """Removes a person from the list by name.

    Args:
        people_list: A list of people, where each person is a list of [name, weight, height].

    Returns:
        The updated list of people.
    """

    name_to_remove = input("Enter the name of the person to remove: ")
    for i in range(len(people_list) - 1, -1, -1):
        if people_list[i][0] == name_to_remove:
            people_list.pop(i)
            print(f"Person '{name_to_remove}' removed.")
            return people_list
    print(f"Person '{name_to_remove}' not found.")
    return people_list

def bmi_status(bmi):
     if bmi < 18.5:
         return 'Laghar'
     elif bmi < 24 and bmi > 18.5:
         return 'Normal'
     elif bmi > 24:
          return 'Chagh'
          
def display_people(people_list):
    """Displays the list of people, including BMI.

    Args:
        people_list: A list of people, where each person is a list of [name, weight, height].
    """

    if not people_list:
        print("No people in the list.")
    else:
        print("People List:")
        for person in people_list:
            bmi = person[1] / (person[2] ** 2)
            bmi_status1 = bmi_status(bmi)
            print(f"Name: {person[0]}, Weight: {person[1]} kg, Height: {person[2]} m, BMI: {bmi:.2f} And you are {bmi_status1}")

def main():
    people = []
    add_person(people,['roli', 63, 1.75])
    add_person(people,['danial', 67, 1.73])
    add_person(people,['arshia', 74, 1.70])

    while True:
        print("\nChoose an option:")
        print("1. Add a person")
        print("2. Remove a person")
        print("3. Display people")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            person_info = get_person_info()
            people = add_person(people, person_info)
        elif choice == '2':
            people = remove_person(people)
        elif choice == '3':
            display_people(people)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
  
