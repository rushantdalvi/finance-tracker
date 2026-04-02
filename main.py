from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud, analytics

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dummy user (for simplicity)
dummy_user = type("User", (), {"id": 1, "role": "admin"})()


@app.post("/transactions")
def create(txn: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, txn, dummy_user.id)


@app.get("/transactions")
def read(db: Session = Depends(get_db)):
    return crud.get_transactions(db, dummy_user.id)


@app.delete("/transactions/{txn_id}")
def delete(txn_id: int, db: Session = Depends(get_db)):
    txn = crud.delete_transaction(db, txn_id)
    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"message": "Deleted"}


@app.get("/summary")
def summary(db: Session = Depends(get_db)):
    txns = crud.get_transactions(db, dummy_user.id)
    return analytics.calculate_summary(txns)