# Dictionary to store membership records. 
# Each key is a unique membership ID.
# The value associated with each key is a nested 
# dictionary containing details about the member, such as their name, 
# age, membership type, and monthly fee.
members = {
    "101": {
        "Name": "Alice Smith", "Age": 25, 
        "Membership Type": "Premium", "Monthly Fee": 100.0},
    "102": {
        "Name": "Bob Johnson", "Age": 30, 
        "Membership Type": "Basic", "Monthly Fee": 30.0},
    "103": {
        "Name": "Charlie Brown", "Age": 22, 
        "Membership Type": "Student", "Monthly Fee": 20.0}
}

# Function to view all membership records. 
# This function iterates through the 
# 'members' dictionary and prints out each member's details in a 
# formatted manner. 
# The for loop goes through each key-value pair in the dictionary, 
# where 'member_id' is the key and 'details' is the nested dictionary.
def view_members():
    for member_id, details in members.items():
        print(
            f"ID: {member_id}, Name: {details['Name']}, Age: {details['Age']}, "
            f"Membership Type: {details['Membership Type']}, Monthly Fee: "
            f"{details['Monthly Fee']}"
            )

# Function to add a new member to the records. 
# This function prompts the user 
# to enter details for a new member, 
# such as their ID, name, age, membership type, and monthly fee. 
# The new details are then added to the 'members' 
# dictionary with the new ID as the key and 
# a nested dictionary of details as the value.
def add_member():
    new_id = input("Enter the new member's ID: ")
    new_name = input("Enter the new member's name: ")
    new_age = int(input("Enter the new member's age: "))
    new_type = input("Enter the desired membership type: ")
    new_fee = float(input("Enter the monthly fee: "))
    members[new_id] = {
        "Name": new_name, "Age": new_age, 
        "Membership Type": new_type, "Monthly Fee": new_fee
    }
    print(f"Member {new_name} added successfully.")

# Function to update the details of an existing member. 
# This function prompts 
# the user to enter the ID of the member they want to update. 
# If the ID exists in the 'members' dictionary, 
# the user is prompted to enter the updated 
# details. The function then updates the nested dictionary 
# for that member with the new details.
def update_member():
    update_id = input("Enter the ID of the member you would like to update: ")
    if update_id in members:
        updated_name = input("Enter the updated name: ")
        updated_age = int(input("Enter the updated age: "))
        updated_type = input("Enter the updated membership type: ")
        updated_fee = float(input("Enter the updated monthly fee: "))
        members[update_id] = {
            "Name": updated_name, "Age": updated_age, 
            "Membership Type": updated_type, "Monthly Fee": updated_fee
        }
        print(f"Member {updated_name} updated successfully.")
    else:
        print("Member not found.")

# Function to delete a member from the records. 
# This function prompts the user 
# to enter the ID of the member they want to delete. 
# If the ID exists in the 'members' dictionary, 
# the corresponding key-value pair is removed from the 
# dictionary.
def delete_member():
    delete_id = input("Enter the ID of the member you would like to delete: ")
    if delete_id in members:
        del members[delete_id]
        print(f"Member {delete_id} deleted successfully.")
    else:
        print("Member not found.")

# Function to search for a specific member by their ID. 
# This function prompts 
# the user to enter the ID of the member they want to search for. 
# If the ID exists in the 'members' dictionary, 
# the function retrieves and prints the 
# member's details from the nested dictionary.
def search_member():
    search_id = input(
        "Enter the ID of the member you would like to search for: "
    )
    if search_id in members:
        details = members[search_id]
        print(
            f"ID: {search_id}, Name: {details['Name']}, \
            Age: {details['Age']}, "
            f"Membership Type: {details['Membership Type']}, Monthly Fee: "
            f"{details['Monthly Fee']}"
        )
    else:
        print("Member not found.")

# Main function to display the menu and handle user choices.
# This function 
# presents the user with a menu of options, allowing them to view, 
# add, update, delete, or search for members. 
# The user's choice is mapped to the 
# corresponding function using the 'options' dictionary,
# and the selected 
# function is called. The loop continues until the user chooses to exit.
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

# Entry point for the program. This block ensures that the 
# 'main' function is 
# only executed if the script is run directly, not imported as
# a module in 
# another script. If the script is run directly,
# it will call the 'main' 
# function to start the program.
if __name__ == "__main__":
    main()
