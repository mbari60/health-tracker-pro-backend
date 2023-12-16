from pydantic import BaseModel

#what the app should accept

class PatientSchema(BaseModel):
    name:str
    phone:int
    age:int
    gender:str
    disease:str
    doseStartDate:str
    doseEndDate:str
    selectedDoctor:str

class dailytrackSchema(BaseModel):
    patNumber:int
    bodyTemperature:str
    bloodPressure:str
    diet:str
    waterIntake:str
    medicationEffectiveness:str
    sleepDuration:str
    nausea:bool
    tiredness:bool
    otherSymptoms:str