def get_person_info():
    """Get a person's name, weight, and height from user input.
    Returns: list [name (str), weight (float or None), height (float or None)] or None if name is empty.
    """
    person = []
    name = input("Enter person's name: ").strip()
    if not name:
        print("\nPerson must have a name.")
        return None

    try:
        weight = input("Enter person's weight (kg): ").strip()
        weight = float(weight) if weight and float(weight) > 0 else None
    except ValueError:
        weight = None

    try:
        height = input("Enter person's height (m): ").strip()
        height = float(height) if height and float(height) > 0 else None
    except ValueError:
        height = None

    return [name, weight, height]

def add_person(people_list, person_info):
    """Adds a person to the list, checking for duplicates by name (case-insensitive).
    Args:
        people_list: List of [name, weight, height] entries.
        person_info: List [name, weight, height] to add.
    Returns: Updated people_list.
    """
    if not person_info:
        return people_list
    name, _, _ = person_info
    name_lower = name.lower()

    for i, person in enumerate(people_list):
        if person[0].lower() == name_lower:
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
    """Removes a person from the list by name (case-insensitive).
    Args:
        people_list: List of [name, weight, height] entries.
    Returns: Updated people_list.
    """
    name_to_remove = input("Enter the name of the person to remove: ").strip().lower()
    for person in people_list[:]:  # Copy list to avoid issues during removal
        if person[0].lower() == name_to_remove:
            people_list.remove(person)
            print(f"\nPerson '{person[0]}' removed.")
            return people_list
    print(f"\nPerson '{name_to_remove}' not found.")
    return people_list

def get_bmi(weight, height):
    """Calculate BMI if weight and height are valid.
    Args:
        weight: Weight in kg (float or None).
        height: Height in meters (float or None).
    Returns: BMI (float) or None if invalid.
    """
    if weight is not None and height is not None and height > 0:
        return weight / (height ** 2)
    return None

def bmi_status(bmi):
    """Return BMI status based on standard medical categories.
    Args:
        bmi: BMI value (float or None).
    Returns: Formatted string with BMI and status, or empty string if BMI is None.
    """
    if bmi is None:
        return ""
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 25:
        status = "Normal"
    elif 25 <= bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"
    return f", BMI: {bmi:.2f}, Status: {status}"

def search(people_list):
    """Search for a person by name (case-insensitive) and display their details.
    Args:
        people_list: List of [name, weight, height] entries.
    """
    name_to_search = input("Enter the name of the person to search: ").strip().lower()
    for person in people_list:
        if person[0].lower() == name_to_search:
            output = f"Name: {person[0]}"
            if person[1] is not None:
                output += f", Weight: {person[1]} kg"
            if person[2] is not None:
                output += f", Height: {person[2]} m"
            bmi = get_bmi(person[1], person[2])
            output += bmi_status(bmi)
            print(output)
            return
    print(f"\nPerson '{name_to_search}' not found.")

def display_people(people_list):
    """Display all people in the list with their details and BMI.
    Args:
        people_list: List of [name, weight, height] entries.
    """
    if not people_list:
        print("No people in the list.")
        return
    print("People List:")
    for person in people_list:
        output = f"Name: {person[0]}"
        if person[1] is not None:
            output += f", Weight: {person[1]} kg"
        if person[2] is not None:
            output += f", Height: {person[2]} m"
        bmi = get_bmi(person[1], person[2])
        output += bmi_status(bmi)
        print(output)

def main():
    """Main function to run the program with a menu-driven interface."""
    people = []
    # Initialize with sample data, ensuring valid types
    add_person(people, ['Roli', 63.0, 1.75])
    add_person(people, ['Danial', 67.0, 1.73])
    add_person(people, ['Arshia', 74.0, 1.70])

    while True:
        print("\nChoose an option:")
        print("1. Add a person")
        print("2. Remove a person")
        print("3. Search a person")
        print("4. Display people")
        print("5. Quit")
        print("--------------------")

        choice = input("Enter your choice: ").strip()
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
            confirm = input("Are you sure you want to quit? (y/n): ").strip()
            if confirm.lower() == 'y':
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()