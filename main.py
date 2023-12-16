from fastapi import FastAPI , Depends ,HTTPException
from sqlalchemy.orm import Session
from schemas import PatientSchema , dailytrackSchema
from database import get_db
from models import  Patient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]
app.add_middleware(CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

#creating a route 
@app.get('/')
def index():
    return {"message": "Hello World"}

#get all events 
@app.get('/patientform')
def get_patients(db:Session = Depends(get_db)):
     Patients = db.query(Patient).all()
     return Patients

@app.get('/patientform/{patient_id}')
def get_patient(patient_id: int , db:Session = Depends(get_db)):
     patient = db.query(Patient).filter(Patient.id==patient_id).first()
     return patient

#posting a patient
@app.post('/patientform')
def create_patient(patient : PatientSchema , db:Session = Depends(get_db)):
    new_patient = Patient(**patient.model_dump())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return {"message": "patient created succesfully", "patient":new_patient}

#posting dailytrack
@app.post('/dailytracks')
def create_patient(dailytrack : dailytrackSchema):
    print(dailytrack)
    return {"message": "daily track submitted succesfully"}

#updating a patient
@app.patch('/patientform/{patient_id}')
def update_patient(patient_id: int):
    return {"message":f"patient {patient_id} created succesfully"}

#updating the daily track
@app.patch('/dailytracks/{patient_id}')
def update_patient(patient_id: int):
    return {"message":f"daily track of patient {patient_id} created succesfully"}

#deleting a patient
@app.delete('/patientform/{phone}')
def delete_patient(phone: str, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.phone == phone).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    db.delete(patient)
    db.commit()
    
    return {"message": "patient deleted successfully", "patient": patient}

#deleting a daily track
@app.delete('/dailytracks/{patient_id}')
def update_patient(patient_id: int):
    return {"message":f"daily track of patient  {patient_id} deleted succesfully"}