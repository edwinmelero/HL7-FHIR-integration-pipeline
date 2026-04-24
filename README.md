# HL7 to FHIR Integration Pipeline (Python)

## Overview
This project demonstrates a real-world healthcare interoperability workflow by converting HL7 v2 ADT messages into FHIR Patient resources using Python.

It simulates how legacy hospital systems communicate with modern API-based healthcare platforms by parsing HL7 messages, transforming the data, and sending it to a live FHIR server.

---

## Architecture

HL7 Message → Python Processing → FHIR JSON → REST API → FHIR Server

---

## Technologies Used

- Python
- HL7 v2 (ADT A01 Message)
- FHIR R4 Standard
- REST API Integration
- JSON Data Transformation

---

## Features

- Parses HL7 v2 ADT messages
- Extracts patient demographic data (name, DOB, gender)
- Transforms HL7 format into FHIR-compliant JSON
- Sends Patient resource to a live FHIR API
- Handles duplicate prevention using unique identifiers
- Demonstrates real-world healthcare data flow

---

## Sample HL7 Message

MSH|^~&|SendingApp|Hospital|ReceivingApp|FHIRServer|202604241200||ADT^A01|12345|P|2.3
PID|1||123456^^^Hospital||Doe^John||19900101|M|||

---

## Sample FHIR Output

```json
{
  "resourceType": "Patient",
  "id": "b45e1626-9d5f-471c-a393-ac4494cd1c45",
  "name": [
    {
      "family": "Doe-930884eb",
      "given": ["John"]
    }
  ],
  "gender": "male",
  "birthDate": "1990-01-01"
}
