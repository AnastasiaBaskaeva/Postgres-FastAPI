from pydantic import BaseModel

# Модель для создания пользователя — используется при вводе
class UserCreate(BaseModel):
    name: str
    email: str

# Модель для отображения пользователя — используется при выводе
class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True  # Позволяет работать с ORM-объектами

# Базовая модель заметки (ввод/обновление)
class NoteBase(BaseModel):
    title: str
    content: str

# Модель создания заметки — дополнительно требует user_id
class NoteCreate(NoteBase):
    user_id: int

# Модель для вывода заметки
class NoteOut(NoteBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True  # Поддержка ORM-объектов