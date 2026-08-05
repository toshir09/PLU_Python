import sqlite3
import heapq
class Patient:
    def __init__(self, patient_id, name, age, priority):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.priority = priority
    def display(self):
        print("Patient ID :", self.patient_id)
        print("Name :", self.name)
        print("Age :", self.age)
        print("Priority Level :", self.priority)
        print("-" * 30)
def fetch_patients():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT patient_id, name, age, priority FROM patients")
    rows = cursor.fetchall()
    conn.close()
    patients = []
    for row in rows:
        patients.append(Patient(row[0], row[1], row[2], row[3]))
    return patients
def delete_patient(patient_id):
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE patient_id = ?", (patient_id,))
    conn.commit()
    conn.close()
patients = fetch_patients()
pq = []
for patient in patients:
    heapq.heappush(pq, (patient.priority, patient.patient_id, patient))
print("Patients Attended")
print("-" * 30)
while pq:
    priority, patient_id, patient = heapq.heappop(pq)
    patient.display()
    delete_patient(patient.patient_id)
print("Remaining Patients")
print("-" * 30)
remaining = fetch_patients()
if len(remaining) == 0:
    print("No patients remaining.")
else:
    for patient in remaining:
        patient.display()