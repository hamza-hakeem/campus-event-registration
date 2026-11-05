from registration_manager import RegistrationManager


def main():
    manager = RegistrationManager()

    while True:
        print("\n===== Campus Event Registration =====")
        print("1. Register Student")
        print("2. List Registrations")
        print("3. Search Registration")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            reg_number = input("Enter registration number: ")
            workshop = input("Enter workshop name: ")

            manager.register_student(name, reg_number, workshop)

        elif choice == "2":
            manager.list_registrations()

        elif choice == "3":
            reg_number = input("Enter registration number to search: ")
            manager.search_registration(reg_number)

        elif choice == "4":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()