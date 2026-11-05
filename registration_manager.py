from registration import Registration


class RegistrationManager:
    def __init__(self):
        self.registrations = []

    def register_student(self, name, reg_number, workshop):
        # Validate empty fields
        if not name.strip() or not reg_number.strip() or not workshop.strip():
            print("Error: All fields are required.")
            return False

        # Prevent duplicate registration numbers
        for student in self.registrations:
            if student.registration_number == reg_number:
                print("Error: Registration number already exists.")
                return False

        # Create and save registration
        student = Registration(name, reg_number, workshop)
        self.registrations.append(student)

        print("Registration successful!")
        return True

    def list_registrations(self):
        if not self.registrations:
            print("No registrations found.")
            return

        print("\n--- Registered Participants ---")
        for student in self.registrations:
            student.display()

    def search_registration(self, reg_number):
        for student in self.registrations:
            if student.registration_number == reg_number:
                print("\nRegistration Found:")
                student.display()
                return student

        print("Error: Registration not found.")
        return None