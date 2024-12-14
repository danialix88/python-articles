def get_person_info():
    """Get a person's name, weight, and height from the user. Returns A list."""
    person = []
    name = input(f"Enter person's name: ")
    weight = input(f"Enter person's weight (kg): ")
    height = input(f"Enter person's height (m): ")
    
    if name:
        person.append(name)
        if weight and weight.isdigit():
            person.append(int(weight))
        else:
            person.append(None)
        if height and height.replace('.', '', 1).isdigit():
            person.append(float(height))
        else:
            person.append(None)
        return person
    else:
        print(f"\nPerson must have name.")

def add_person(people_list, person_info):
    """Adds a person to the list, checking for duplicates."""
    name, _, _ = person_info

    for i, person in enumerate(people_list):
        if person[0] == name:
            overwrite = input(f"\nPerson with name '{name}' already exists. Overwrite? (y/n): ")
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
    """Removes a person from the list by name."""
    name_to_remove = input("Enter the name of the person to remove: ")
    for i in range(len(people_list) - 1, -1, -1):
        if people_list[i][0] == name_to_remove:
            people_list.pop(i)
            print(f"\nPerson '{name_to_remove}' removed.")
            return people_list
    print(f"\nPerson '{name_to_remove}' not found.")
    return people_list

def get_bmi(weight, height):
    """Calculate BMI"""
    if height and weight:
        return weight / (height ** 2)
    else:
        return False

def bmi_status(bmi):
    """Retrun BMI Status."""
    if bmi < 18.5:
        status = 'Skinny'
    elif 18.5 <= bmi < 24:
        status = 'Normal'
    else:
        status = 'Fat'
    return f", BMI: {bmi:.2f} And you are {status}"

def search(people_list):
    """Search a person in list of people, By name."""
    name_to_search = input("Enter the name of the person to search: ")
    for person in people_list:
        if person[0] == name_to_search:
            print(f"Name: {person[0]}", end="")
            if person[1]:
                print(f", Weight: {person[1]} kg", end="")
            if person[2]:
                print(f", Height: {person[2]} m", end="")
            if person[1] and person[2]:
                bmi = get_bmi(person[1], person[2])
                print(f"{bmi_status(bmi)}")
            return
    print(f"\nPerson '{name_to_search}' not found.")

def display_people(people_list):
    """Displays the list of people, including BMI."""
    if not people_list:
        print("No people in the list.")
    else:
        print("People List:")
        for person in people_list:
            print(f"Name: {person[0]}", end="")
            if person[1]:
                print(f", Weight: {person[1]} kg", end="")
            if person[2]:
                print(f", Height: {person[2]} m", end="")
            if person[1] and person[2]:
                bmi = get_bmi(person[1], person[2])
                print(f"{bmi_status(bmi)}")
            print()  # New line for better readability

def main():
    people = []
    add_person(people, ['roli', 63, 1.75])
    add_person(people, ['danial', 67, 1.73])
    add_person(people, ['arshia', 74, 1.70])

    while True:
        print("\nChoose an option:")
        print("1. Add a person")
        print("2. Remove a person")
        print("3. Search a person")
        print("4. Display people")
        print("5. Quit")
        print("--------------------")

        choice = input("Enter your choice: ")

        if choice == '1':
            person_info = get_person_info()
            if person_info:
                people = add_person(people, person_info)
        elif choice == '2':
            people = remove_person(people)
        elif choice == '3':
            search(people)
        elif choice == '4':
            display_people(people)
        elif choice == '5':
            confirm = input("Are you sure you want to quit? (y/n): ")
            if confirm.lower() == 'y':
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
