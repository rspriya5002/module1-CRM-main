## app/repos/lead_repo.py
from app.models import Lead

class LeadRepo:
    def get(self, session, lead_id: int):
        return session.query(Lead).filter(Lead.id == lead_id).first()

    def create(self, session, lead_data: dict):
        lead = Lead(**lead_data)
        session.add(lead)
        session.flush()
        session.refresh(lead)
        return lead  # let service handle commit/refresh

    def list_all(self, session, limit=100):
        return (
            session.query(Lead)
            .order_by(Lead.created_at.desc())
            .limit(limit)
            .all()
        )
