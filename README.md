**OVERVIEW**

A RESTful API using Django that serves as a backend for a hypothetical patient directory management application.

**REQUIREMENTS**
1. Dockerize the application
2. Provide unit tests for the API endpoints
3. Data Model: Patient object model must include all of the following fields: id, first_name, last_name, gender, date_of_birth, age, status (e.g., active, inactive).
4. Endpoint
- GET `/patients` - List all patients.
- POST `/patients` - Create a new patient. (Before saving the patient data in the database, calculate the patient’s age based on the patient’s date of birth and save their age in the age field. Create custom function.)
- GET `/patients/<id>` - Get a single patient by ID.
- PUT `/patients/<id>` - Update a patient by ID.
- DELETE `/patients/<id>` - Delete a patient by ID.

**Sample data format:**

            "id": "e99165f0-9b69-47a4-ba57-fe878e62db26",
            "first_name": "Minh",
            "last_name": "Hudson",
            "date_of_birth": "1988-03-14",
            "gender": "F",
            "age": 36,
            "status": true

- `id`: UUID format.
- `gender`: 1 character length is better than 4-6 characters length value while saving into the database table. However, we can display 'Male' instead of 'M' (for example) in frontend. Gender can be 'Male', 'Female', and 'Other'.
- `status`: Boolean is the best type if there are two options. 'status' field has two options (true for active, false for inactive).

**Instructions on how to deploy project:**

1. Create a folder in your machine. You may name it as `myPatient` if you want.
2. Inside `myPatient` (or your created folder) download and unzip `patient_directory` folder.
3. Open IDE or terminal and go to `patient_directory` location by running command: `cd patient_directory`
4. Run docker command to start: `docker compose up -d --build`
5. Go to http://localhost:8000/ for intro page
6. Go to http://localhost:8000/patients/ for `/patients` endpoint: create new patient (POST), List all patients (GET).
7. Go to http://localhost:8000/patients/81948da6-66f4-4352-ae17-7b46cb4707ec (example) for `/patients/<id>` endpoint: view (GET), fully update (PUT), partially update (PATCH), delete (DELETE) patient using ID. 
8. Run docker command to stop: `docker compose down`

**Instructions on how to test project:**
1. Go to 'patient_directory' folder (if you are not there) by running command: `cd patient_directory`
2. Run command for testing: `python manage.py test`

