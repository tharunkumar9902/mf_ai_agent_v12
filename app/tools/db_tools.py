from sqlalchemy.orm import Session
from app.db.crud import save_chat_history, get_chat_history

def save_chat(db: Session, user_id: str, query: str, answer: str):
    return save_chat_history(db, user_id, query, answer)

def fetch_history(db: Session, user_id: str):
    return get_chat_history(db, user_id)
