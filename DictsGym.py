members = {
    "101": {"Name": "Alice Smith", "Age": 25, "Membership Type": "Premium", "Monthly Fee": 100.0},
    "102": {"Name": "Bob Johnson", "Age": 30, "Membership Type": "Basic", "Monthly Fee": 30.0},
    "103": {"Name": "Charlie Brown", "Age": 22, "Membership Type": "Student", "Monthly Fee": 20.0}
}

def view_members():
    for member_id, details in members.items():
        print(f"ID: {member_id}, Name: {details['Name']}, Age: {details['Age']}, "
              f"Membership Type: {details['Membership Type']}, Monthly Fee: {details['Monthly Fee']}")

def add_member():
    new_id = input("Enter the new member's ID: ")
    new_name = input("Enter the new member's name: ")
    new_age = int(input("Enter the new member's age: "))
    new_type = input("Enter the desired membership type: ")
    new_fee = float(input("Enter the monthly fee: "))
    members[new_id] = {"Name": new_name, "Age": new_age, "Membership Type": new_type, "Monthly Fee": new_fee}
    print(f"Member {new_name} added successfully.")

def update_member():
    update_id = input("Enter the ID of the member you would like to update: ")
    if update_id in members:
        updated_name = input("Enter the updated name: ")
        updated_age = int(input("Enter the updated age: "))
        updated_type = input("Enter the updated membership type: ")
        updated_fee = float(input("Enter the updated monthly fee: "))
        members[update_id] = {"Name": updated_name, "Age": updated_age, "Membership Type": updated_type, "Monthly Fee": updated_fee}
        print(f"Member {updated_name} updated successfully.")
    else:
        print("Member not found.")

def delete_member():
    delete_id = input("Enter the ID of the member you would like to delete: ")
    if delete_id in members:
        del members[delete_id]
        print(f"Member {delete_id} deleted successfully.")
    else:
        print("Member not found.")

def search_member():
    search_id = input("Enter the ID of the member you would like to search for: ")
    if search_id in members:
        details = members[search_id]
        print(f"ID: {search_id}, Name: {details['Name']}, Age: {details['Age']}, "
              f"Membership Type: {details['Membership Type']}, Monthly Fee: {details['Monthly Fee']}")
    else:
        print("Member not found.")

def main():
    print("Hello, welcome to the Gym management system")
    options = {
        1: view_members,
        2: add_member,
        3: update_member,
        4: delete_member,
        5: search_member,
        6: exit
    }

    while True:
        try:
            print("Option 1. View membership records.")
            print("Option 2. Add a new member.")
            print("Option 3. Update an existing member.")
            print("Option 4. Delete a member record.")
            print("Option 5. Search for a member.")
            print("Option 6. Exit the program.")
            choice = int(input("What would you like to do? (1-6): "))

            if choice in options:
                options[choice]()
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Enter a valid number.")

if __name__ == "__main__":
    main()
