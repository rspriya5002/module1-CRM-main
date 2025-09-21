from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.schemas import LeadCreate, PromoteRequest
from app.repos.lead_repo import LeadRepo
from app.repos.deal_repo import DealRepo
from app.services.lead_service import LeadService

router = APIRouter(prefix="/leads")

# Instantiate repos once
lead_repo = LeadRepo()
deal_repo = DealRepo()
# Create the service instance
svc = LeadService(lead_repo, deal_repo, SessionLocal)

@router.post("/", response_model=dict, status_code=201)
def create_lead(payload: LeadCreate):
    
    return svc.create_lead(payload.name, payload.email)

@router.post("/{lead_id}/promote", status_code=201)
def promote(lead_id: int, payload: PromoteRequest):
   
    try:
        deal = svc.promote_to_deal(lead_id, payload.value_cents, payload.seller_id)
        return {"deal_id": deal.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
