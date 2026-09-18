practitioners = []
patients = []
appointments = []

def practitioner(id, name):
    practitioners.append([id, name])

def appointment(id, date, time, practitioner, patient):
    appointments.append([id, date, time, practitioner, patient])

def patient(id, name, dob, gender):
    patients.append([id, name, dob, gender])

practitioner(123, "Joe")
practitioner(124, "Jill")
appointment(12, 22/8/2026, 1600, 123, 32)
patient(32, "Jack", 28/2/1989, "M")

print(practitioners)