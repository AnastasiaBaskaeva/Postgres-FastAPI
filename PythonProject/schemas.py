from pydantic import BaseModel

class Quote(BaseModel):     # это типо для валидации данных чтоб четко по этому шаблонууу
    author : str
    message : str