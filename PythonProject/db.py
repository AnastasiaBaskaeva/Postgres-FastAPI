from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL = "postgresql+psycopg2://postgres:postgres@192.168.56.101:5432/bsbo30"    # юрл постгреха

engine = create_engine(URL)    # энджн это типо точка подключения к базе 
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False) # а это типо сессия подключения через точку
Base = declarative_base() # бывают разные схемы данных - это декларатиавня // это нужно короче для того чтобы модель таблицы унаследолвала