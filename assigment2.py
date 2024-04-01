class Patient:
    def __init__(self, name, age, condition):
        self.name = name
        self.age = age
        self.condition = condition

class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

class Prescription:
    def __init__(self, medicine, dosage):
        self.medicine = medicine
        self.dosage = dosage

class Hospital:
    def __init__(self):
        self.patient_records = []
        self.doctors = []
        self.queue = []

    def add_patient(self, patient):
        self.patient_records.append(patient)

    def update_patient(self, name, new_condition):
        for patient in self.patient_records:
            if patient.name == name:
                patient.condition = new_condition
                print("Patient updated successfully.")
                return
        print("Patient not found.")

    def remove_patient(self, name):
        for patient in self.queue:
            if patient.name == name:
                self.queue.remove(patient)
                print("Patient removed from the queue.")
                return
        print("Patient not found in the queue.")

    def display_queue(self):
        print("Patients waiting for the doctor:")
        for patient in self.queue:
            print(patient.name)

    def add_to_queue(self, patient):
        self.queue.append(patient)
        print("Patient added to the queue.")

    def display_patient_records(self):
        print("List of patients:")
        for patient in self.patient_records:
            print(f"Name: {patient.name}, Age: {patient.age}, Condition: {patient.condition}")

# Menu interface
def main_menu():
    print("1. Add a new patient")
    print("2. Update patient information")
    print("3. Remove patient from queue")
    print("4. Show patients waiting for doctor")
    print("5. Show patient records")
    print("6. Exit")

hospital = Hospital()

while True:
    print("\nWelcome to the Hospital Management System")
    main_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter patient's name: ")
        age = int(input("Enter patient's age: "))
        condition = input("Enter patient's condition: ")
        patient = Patient(name, age, condition)
        hospital.add_patient(patient)

    elif choice == "2":
        name = input("Enter patient's name: ")
        new_condition = input("Enter new condition: ")
        hospital.update_patient(name, new_condition)

    elif choice == "3":
        name = input("Enter patient's name: ")
        hospital.remove_patient(name)

    elif choice == "4":
        hospital.display_queue()

    elif choice == "5":
        hospital.display_patient_records()

    elif choice == "6":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

# Documentation
"""
Documentation:
Data Structure Implementation:
- Patient, Doctor, Prescription, and Hospital are different parts of the system.
- They help to organize information about patients, doctors, and prescriptions.

Basic Functionality:
- We can add new patients, update patient records, remove patients from the waiting list, and display information about patients.
- The system is menu-based for easy use.

Usage Instructions:
- Choose options from the menu to interact with the system.
- Follow the prompts to add, update, or remove patients, and to display patient information.
- You can exit the program by selecting the appropriate option.
"""