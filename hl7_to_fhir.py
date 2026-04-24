import hl7
import requests
import json
import uuid

patient_id = str(uuid.uuid4())

print("Starting HL7 → FHIR process...")

# Read HL7 file
with open("sample.hl7", "r") as file:
    hl7_data = file.read()

print("\nHL7 message loaded:\n")
print(hl7_data)

# Parse HL7
print("Parsing HL7 manually...")

segments = hl7_data.strip().split("\n")

pid_segment = None

for seg in segments:
    if seg.startswith("PID"):
        pid_segment = seg
        break

if pid_segment is None:
    raise Exception("PID segment not found")

print("PID found:", pid_segment)

pid_fields = pid_segment.split("|")

last_name = pid_fields[5].split("^")[0]
first_name = pid_fields[5].split("^")[1]
dob = pid_fields[7]
gender = pid_fields[8]

print("\nExtracted Values:")
print("First Name:", first_name)
print("Last Name:", last_name)
print("DOB:", dob)
print("Gender:", gender)



# Build FHIR Patient
import uuid

unique_suffix = str(uuid.uuid4())[:8]

patient = {
    "resourceType": "Patient",
    "id": patient_id,
    "name": [{
        "family": f"{last_name}-{unique_suffix}",
        "given": [first_name]
    }],
    "gender": "male" if gender == "M" else "female",
    "birthDate": dob[:4] + "-" + dob[4:6] + "-" + dob[6:8]
}
# Send to FHIR server


url = f"https://hapi.fhir.org/baseR4/Patient/{patient_id}"

headers = {
    "Content-Type": "application/fhir+json"
}

print("\nSending to FHIR server...")

response = requests.put(url, headers=headers, data=json.dumps(patient))

print("\nFHIR Response:")
print("Status Code:", response.status_code)
print(response.text)

print("\nProcess complete.")
