from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URI = "postgresql+psycopg2://postgres:m03kht4r1999@127.0.0.1:5432/fastapidb"

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
s = Session()

Base = declarative_base()

Base.metadata.create_all(engine)