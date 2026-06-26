from sqlalchemy.orm import Session
from app.db.models import ChatHistory

def save_chat_history(db: Session, user_id: str, query: str, agent_response: str):
    chat = ChatHistory(user_id=user_id, query=query, agent_response=agent_response)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat

def get_chat_history(db: Session, user_id: str):
    return db.query(ChatHistory).filter(ChatHistory.user_id == user_id).order_by(ChatHistory.created_at.desc()).all()
