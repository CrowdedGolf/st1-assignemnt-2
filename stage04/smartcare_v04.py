import uuid
practitioners = []
patients = []
appointments = []

def practitioner(id, name):
    if not id:
        raise ValueError("ID field cannot be empty.")
    if not name:
        raise ValueError("Name field cannot be empty.")
    practitioners.append([id, name])

def create_appointment(date_time, practitioner_id, patient_id, cancelled):
    appointment = {
        "appointment_id": str(uuid.uuid4()),
        "date_time": date_time,
        "practitioner_id": practitioner_id,
        "patient_id": patient_id,
        "cancelled": cancelled,
    }

    appointments.append(appointment)

def patient(id, name, dob, gender):
    if not id:
        raise ValueError("ID field cannot be empty.")
    if not name:
        raise ValueError("Name field cannot be empty.")
    if not dob:
        raise ValueError("Date of birth field cannot be empty")
    if not gender:
        raise ValueError("Gender field cannot be empty.")
    patients.append([id, name, dob, gender])

practitioner(123, "Joe")
practitioner(124, "Jill")
create_appointment("22-8-2026 16:00", 123, 32, False)
create_appointment("22-8-2026 17:00", 113, 35, False)
patient(32, "Jack", 28/2/1989, "M")

print(appointments)