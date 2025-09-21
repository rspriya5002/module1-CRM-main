# app/repos/deal_repo.py
from app.models import Deal

class DealRepo:
    def get(self, session, deal_id: int):
        return session.query(Deal).filter(Deal.id == deal_id).first()

    def create(self, session, deal_data: dict):
        deal = Deal(**deal_data)
        session.add(deal)
        return deal  # let service handle commit/refresh

    def list_all(self, session, limit=100):
        return (
            session.query(Deal)
            .order_by(Deal.created_at.desc())
            .limit(limit)
            .all()
        )
