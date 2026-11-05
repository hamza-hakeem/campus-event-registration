from registration import Registration


class RegistrationManager:
    def __init__(self):
        self.registrations = []

    def register_student(self, name, reg_number, workshop):
        if not name.strip() or not reg_number.strip() or not workshop.strip():
            print("Error: All fields are required.")
            return

        for student in self.registrations:
            if student.registration_number == reg_number:
                print("Error: Duplicate registration number.")
                return

        student = Registration(name, reg_number, workshop)
        self.registrations.append(student)

        print("Registration successful!")

    def list_registrations(self):
        if not self.registrations:
            print("No registrations found.")
            return

        for student in self.registrations:
            print("Name:", student.name)
            print("Registration Number:", student.registration_number)
            print("Workshop:", student.workshop)
            print("--------------------")

            def search_registration(self, reg_number):
                for student in self.registrations:
                 if student.registration_number == reg_number:
                     print("Registration Found!")
                     print("Name:", student.name)
                     print("Registration Number:", student.registration_number)
                     print("Workshop:", student.workshop)
                     return

            print("Registration not found.")

            def search_registration(self, reg_number):
                for student in self.registrations:
                    if student.registration_number == reg_number:
                        print("Registration Found!")
                        print("Name:", student.name)
                        print("Registration Number:", student.registration_number)
                        print("Workshop:", student.workshop)
                        return student

                print("Registration not found.")
                return None