from fastapi import FastAPI , Depends ,HTTPException
from sqlalchemy.orm import Session
from schemas import PatientSchema , dailytrackSchema
from database import get_db
from models import  Patient , DailyTrack
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

#get all patients
@app.get('/patientform')
def get_patients(db:Session = Depends(get_db)):
     Patients = db.query(Patient).all()
     return Patients
#get all dailytracks
@app.get('/dailytracks')
def get_dailytracks(db:Session = Depends(get_db)):
    dailytracks = db.query(DailyTrack).all()
    return dailytracks

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
def create_daily_track(dailytrack: dailytrackSchema, db: Session = Depends(get_db)):
    # Checking if the patient with the given phone number exists
    patient = db.query(Patient).filter(Patient.phone == dailytrack.patNumber).first()
    #adding the dailytrack if the patient exists
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    new_daily_track = DailyTrack(**dailytrack.model_dump(), patient_id=patient.id)
    db.add(new_daily_track)
    db.commit()
    db.refresh(new_daily_track)

    return {"message": "Daily track submitted successfully"}

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
def delete_patient(phone: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.phone == phone).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    #deleting associated dailytack of the patient
    db.query(DailyTrack).filter(DailyTrack.patient_id == patient.id).delete()

    db.delete(patient)
    db.commit()
    
    return {"message": "patient deleted successfully", "patient": patient}

#deleting a daily track
@app.delete('/dailytracks/{patNumber}')
def delete_daily_tracks(patNumber: int, db: Session = Depends(get_db)):
    db.query(DailyTrack).filter(DailyTrack.patNumber == patNumber).delete()
    db.commit()
    return {"message": f"DailyTracks for Patient ID {patNumber} deleted successfully"}
