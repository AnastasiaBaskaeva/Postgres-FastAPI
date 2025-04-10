
from sqlalchemy.orm import Session
from models import User, Note
from schemas import UserCreate, NoteCreate, NoteBase

# Создание пользователя
def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email)  # создаем ORM-объект
    db.add(db_user)      # добавляем в сессию
    db.commit()          # сохраняем изменения
    db.refresh(db_user)  # обновляем объект, чтобы получить id
    return db_user

# Получение всех пользователей
def get_users(db: Session):
    return db.query(User).all()

# Получение одного пользователя по id
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Создание заметки
def create_note(db: Session, note: NoteCreate):
    db_note = Note(**note.dict())  # распаковка полей через .dict()
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

# Получение всех заметок
def get_notes(db: Session):
    return db.query(Note).all()

# Получение одной заметки по id
def get_note(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()

# Получение всех заметок по user_id
def get_notes_by_user(db: Session, user_id: int):
    return db.query(Note).filter(Note.user_id == user_id).all()

# Обновление заметки по id
def update_note(db: Session, note_id: int, data: NoteBase):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note:
        db_note.title = data.title
        db_note.content = data.content
        db.commit()
        db.refresh(db_note)
    return db_note

# Удаление заметки по id
def delete_note(db: Session, note_id: int):
    db_note = db.query(Note).filter(Note.id == note_id).first()
    if db_note:
        db.delete(db_note)
        db.commit()
    return db_note
