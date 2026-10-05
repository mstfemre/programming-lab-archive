class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def __str__(self):
        return f"{self.name}, {self.age} years old"


class Doctor(Person):
    def __init__(self, name, age, specialty, consultation_fee):
        super().__init__(name, age)
        self.specialty = specialty
        self.__consultation_fee = consultation_fee

    def examine(self):
        print(f"Dr. {self.name} is examining a patient in {self.specialty}.")

    def get_consultation_fee(self):
        return self.__consultation_fee

    def introduce(self):
        print(
            f"Hello, my name is {self.name} and I am {self.age} years old. "
            f"Specialty: {self.specialty}"
        )

    def __str__(self):
        return f"Dr. {self.name} ({self.specialty})"


class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id = patient_id
        self._temperatures = []

    def add_temperature(self, temp):
        self._temperatures.append(temp)

    def get_average_temperature(self):
        if not self._temperatures:
            return 0
        return sum(self._temperatures) / len(self._temperatures)

    def has_fever(self):
        return self.get_average_temperature() >= 37.5

    def introduce(self):
        print(
            f"Hello, my name is {self.name} and I am {self.age} years old. "
            f"ID: {self.patient_id}"
        )

    def __str__(self):
        avg_temp = self.get_average_temperature()
        fever_status = "Yes" if self.has_fever() else "No"
        return (
            f"{self.name} (ID: {self.patient_id}) - "
            f"Avg Temp: {avg_temp:.1f}C - Fever: {fever_status}"
        )


class Ward:
    def __init__(self, ward_number, doctor):
        self.ward_number = ward_number
        self.doctor = doctor
        self.patients = []

    def admit_patient(self, patient):
        self.patients.append(patient)

    def discharge_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                self.patients.remove(patient)
                return patient
        return None

    def ward_average_temperature(self):
        if not self.patients:
            return 0

        total = sum(patient.get_average_temperature() for patient in self.patients)
        return total / len(self.patients)

    def display_info(self):
        print(f"=== Ward {self.ward_number} ===")
        print(f"Doctor: {self.doctor}")
        print()

        print("--- Introductions (polymorphism) ---")
        people_in_ward = [self.doctor] + self.patients

        for person in people_in_ward:
            person.introduce()

        print()
        print("Patients:")
        for patient in self.patients:
            print(patient)

        print()
        print(f"Ward Average Temperature: {self.ward_average_temperature():.1f}C")

    def __str__(self):
        return (
            f"Ward {self.ward_number} has Dr. {self.doctor.name} "
            f"and {len(self.patients)} patient(s)."
        )


def find_highest_fever_patient(patients):
    if not patients:
        return None

    return max(patients, key=lambda patient: patient.get_average_temperature())


def group_by_fever_status(patients):
    groups = {"fever": [], "no_fever": []}

    for patient in patients:
        if patient.has_fever():
            groups["fever"].append(patient)
        else:
            groups["no_fever"].append(patient)

    return groups


def show_fever_groups(groups):
    fever_names = [patient.name for patient in groups["fever"]]
    no_fever_names = [patient.name for patient in groups["no_fever"]]

    return {"fever": fever_names, "no_fever": no_fever_names}


doctor = Doctor("Johnson", 45, "Cardiology", 500)

emma = Patient("Emma", 30, "P001")
emma.add_temperature(38.0)
emma.add_temperature(38.4)

liam = Patient("Liam", 25, "P002")
liam.add_temperature(36.7)
liam.add_temperature(36.9)

olivia = Patient("Olivia", 40, "P003")
olivia.add_temperature(37.5)
olivia.add_temperature(37.7)

ward = Ward(204, doctor)
ward.admit_patient(emma)
ward.admit_patient(liam)
ward.admit_patient(olivia)

ward.display_info()

highest_patient = find_highest_fever_patient(ward.patients)
print(
    f"Highest Fever: {highest_patient.name} "
    f"({highest_patient.get_average_temperature():.1f}C)"
)

fever_groups = group_by_fever_status(ward.patients)
print(f"Grouped by fever: {show_fever_groups(fever_groups)}")
