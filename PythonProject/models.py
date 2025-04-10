from sqlalchemy import Column, Integer, String, Boolean
from db import Base

class Quote(Base): # это корчче модель таблицы для датабазы
    __tablename__ = "stado"
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String)
    message = Column(String)

