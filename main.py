from registration_manager import RegistrationManager

manager = RegistrationManager()

while True:
    print("\nCampus Event Registration System")
    print("1. Register Student")
    print("2. Display Registrations")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        reg_number = input("Enter registration number: ")
        workshop = input("Enter workshop name: ")

        manager.register_student(name, reg_number, workshop)

    elif choice == "2":
        manager.list_registrations()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")