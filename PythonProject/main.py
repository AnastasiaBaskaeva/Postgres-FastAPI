from fastapi import  FastAPI, HTTPException
from db import notes
from models import Note
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@192.168.56.101:5432/bsbo30"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


app = FastAPI()

@app.get("/notes")
def get_all_notes():
    return notes

@app.get("/notes/{note_id}")
def get_note_by_id(note_id: int):
    if note_id < 0 or note_id > len(notes):
        return HTTPException(status_code=400, detail="Id doe not be < 0 or > len of notes")
    return notes[note_id]

@app.get("/search_user")
def search_by_user(keyword: str):
    results = [note for note in notes if keyword.lower() in note.user.lower()]
    return results
@app.get("/search_message")
def search_by_message(keyword: str):
    results = [note for note in notes if keyword.lower() in note.message.lower()]
    return results

@app.post("/notes")
def create_new_note(note: Note):
    notes.append(note)
    return {"id": len(notes) - 1, "note": note}

@app.post("/change_user")
def change_user(keyword: str, new_user: str):
    for note in notes:
        if keyword.lower() in note.user.lower():
            note.user = new_user

@app.post("/change_message")
def change_message(keyword: str, new_message: str):
    for note in notes:
        if keyword.lower() in note.message.lower():
            note.message = new_message

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id < 0 or note_id > len(notes):
        return HTTPException(status_code=400, detail="Id doe not be < 0 or > len of notes")
    deleted = notes.pop(note_id)
    return {"message": "Note deleted", "note": deleted}
