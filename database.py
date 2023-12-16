from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://admin:pk6OBIDckrYHYiaNNQvhVxVql2gODwwg@dpg-clun3pla73kc73bimkpg-a.frankfurt-postgres.render.com/health_b7t6", echo=True)

local_session = sessionmaker(bind=engine)

def get_db():
    db=local_session()
    try:
        yield db
    finally:
        db.close()