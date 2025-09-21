# app/services/lead_service.py
class LeadService:
    def __init__(self, lead_repo, deal_repo, session_factory):
        self.lead_repo = lead_repo
        self.deal_repo = deal_repo
        self.session_factory = session_factory  # e.g., SessionLocal

    def create_lead(self, name: str, email: str):
        with self.session_factory() as session:
            lead_data = {"name": name, "email": email, "status": "new"}
            lead = self.lead_repo.create(session, lead_data)
            session.commit()
            session.refresh(lead)
            return {"id": lead.id, "name": lead.name, "email": lead.email, "status": lead.status}

    def promote_to_deal(self, lead_id: int, value_cents: int, seller_id: int | None = None):
        with self.session_factory() as session:
            lead = self.lead_repo.get(session, lead_id)
            if not lead:
                raise ValueError("Lead not found")
            lead.status = "promoted"
            deal_data = {"lead_id": lead.id, "value_cents": value_cents, "seller_id": seller_id}
            deal = self.deal_repo.create(session, deal_data)
            session.commit()
            session.refresh(deal)
            return deal
