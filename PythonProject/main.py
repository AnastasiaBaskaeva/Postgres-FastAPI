from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import engine, SessionLocal
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():  # корчое так мы к бд обращаемя я так понял
    db = SessionLocal()
    try:
        yield db  # йилд(урожай) типо для того чтобы можно было обращаться вот так: for i in get_db() ?????
    finally:
        db.close()


@app.get("/quotes/")
async def get_quotes(db: Session = Depends(get_db)):  # ??????? дб это наша дб /// зачем депендс
    try:
        return db.query(models.Quote).all()  # типо квери по модели но модель это типо наш дб че нахуй
    except:
        raise HTTPException(404)


@app.get("/notes/{index}")
async def get_quote(index: int, db: Session = Depends(get_db)):
    try:
        index = int(index)
        return db.query(models.Quote).get(index)
    except:
        raise HTTPException(404)


@app.post("/quotes/")
async def post_quote(quote: schemas.Quote, db: Session = Depends(get_db)):
    try:
        db_quote = models.Quote(
            **quote.dict())  # тут мы преобразуем нашу цитату в вид для бд походу в модели(которая является начледникос Base) есть сектренытй метод который принмает kwargs
        db.add(db_quote)
        db.commit()
        db.refresh(db_quote)
        return db_quote
    except:
        raise HTTPException(400)


@app.put("/quotes/{index}")
async def edit_quote(index: int, edited_quote: schemas.Quote, db: Session = Depends(get_db)):
    try:
        index = int(index)
        db_quote = db.query(models.Quote).get(index)

        db_quote.text = edited_quote.text
        db_quote.author = edited_quote.author
        db_quote.rating = edited_quote.rating

        db.commit()
        db.refresh(db_quote)
        return db_quote
    except:
        raise HTTPException(400)


@app.delete("/delete/{index}")
async def delete_quote(index: int, db: Session = Depends(get_db)):
    try:
        index = int(index)
        db_quote = db.query(models.Quote).get(index)
        db.delete(db_quote)
        db.commit
        db.refresh(db_quote)
        raise HTTPException(200)
    except:
        raise HTTPException(404)