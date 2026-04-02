from sqlalchemy.orm import Session
from models import Transaction


def create_transaction(db: Session, txn, user_id: int):
    db_txn = Transaction(**txn.dict(), user_id=user_id)
    db.add(db_txn)
    db.commit()
    db.refresh(db_txn)
    return db_txn


def get_transactions(db: Session, user_id: int):
    return db.query(Transaction).filter(Transaction.user_id == user_id).all()


def delete_transaction(db: Session, txn_id: int):
    txn = db.query(Transaction).filter(Transaction.id == txn_id).first()
    if not txn:
        return None
    db.delete(txn)
    db.commit()
    return txn