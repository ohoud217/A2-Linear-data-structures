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
                print("Patient record updated successfully.")
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
        print("Patients in queue:")
        for patient in self.queue:
            print(patient.name)

    def add_to_queue(self, patient):
        self.queue.append(patient)
        print("Patient added to the queue.")

    def display_patient_records(self):
        print("Patient Records:")
        for patient in self.patient_records:
            print(f"Name: {patient.name}, Age: {patient.age}, Condition: {patient.condition}")


# Sample usage
if __name__ == "__main__":
    hospital = Hospital()

    # Adding patients
    patient1 = Patient("Lama", 27, "Arm injury")
    patient2 = Patient("Mara", 43, "Fever")
    hospital.add_patient(patient1)
    hospital.add_patient(patient2)

    # Updating patient record
    hospital.update_patient("Lama", "Broken arm")

    # Displaying patient records
    hospital.display_patient_records()

