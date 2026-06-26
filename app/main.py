from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.routes import router as app_router
from app.api.health import router as health_router
from app.api.reports import router as reports_router
from app.core.logging_config import setup_logging

setup_logging()
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mutual Fund AI Agent", version="1.2.0")
app.include_router(health_router)
app.include_router(app_router)
app.include_router(reports_router)
