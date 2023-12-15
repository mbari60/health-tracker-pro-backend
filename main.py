from fastapi import FastAPI

app = FastAPI()
 
#creating a route 
@app.get('/')
def index():
    return {"message": "Hello World"}

#get all events 
@app.get('/patientform')
def get_patients():
     return []

@app.get('/patientform/{patient_id}')
def get_patient():
     return {}

#posting a patient
@app.post('/patientform')
def create_patient():
    return {"message": "patient created succesfully"}

#updating a patient
@app.patch('/patientform/{patient_id}')
def update_patient(patient_id: int):
    return {"message":f"patient {patient_id} created succesfully"}

#deleting a patient
@app.delete('/patientform/{patient_id}')
def update_patient(patient_id: int):
    return {"message":f"patient {patient_id} deleted succesfully"}