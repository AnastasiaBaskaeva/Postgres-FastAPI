from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

# ORM-модель для таблицы пользователей
class User(Base):
    __tablename__ = "users"  # Название таблицы в базе

    id = Column(Integer, primary_key=True, index=True)  # Первичный ключ
    name = Column(String)  # Имя пользователя
    email = Column(String, unique=True, index=True)  # Уникальный email
    notes = relationship("Note", back_populates="owner")  # Связь с заметками

# ORM-модель для таблицы заметок
class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)  # Первичный ключ
    title = Column(String, index=True)  # Заголовок заметки
    content = Column(String)  # Содержание заметки
    user_id = Column(Integer, ForeignKey("users.id"))  # Внешний ключ на пользователя

    owner = relationship("User", back_populates="notes")  # Обратная связь
