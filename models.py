from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Text , Integer ,DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Patient(Base):
    __tablename__="patients"
    id=Column(Integer(),primary_key=True)
    name=Column(Text(),nullable=False)
    phone=Column(Integer(),nullable=False,unique=True)
    age=Column(Integer(),nullable=False)
    gender=Column(Text(),nullable=False)
    disease=Column(Text(),nullable=False)
    doseStartDate=Column(DateTime(),nullable=False)
    doseEndDate=Column(DateTime(),nullable=False)
    selectedDoctor=Column(Text(),nullable=False)

    daily_tracks = relationship('DailyTrack', back_populates='patient')

class DailyTrack(Base):
    __tablename__ = "dailytrack"
    id = Column(Integer(), primary_key=True)
    patNumber = Column(Integer(), nullable=False)
    bodyTemperature = Column(Text(), nullable=False)
    bloodPressure = Column(Text(), nullable=False)
    diet = Column(Text(), nullable=False)
    waterIntake = Column(Text(), nullable=False)
    medicationEffectiveness = Column(Text(), nullable=False)
    sleepDuration = Column(Text(), nullable=False)
    nausea = Column(Boolean(), nullable=False)
    tiredness = Column(Boolean(), nullable=False)
    otherSymptoms = Column(Text(), nullable=False)

    patient_id = Column(Integer, ForeignKey('patients.id'))
    patient = relationship('Patient', back_populates='daily_tracks')


