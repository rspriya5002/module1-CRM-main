from pydantic import BaseModel, EmailStr, ConfigDict

class LeadCreate(BaseModel):
    name: str
    email: EmailStr | None = None


class LeadOut(BaseModel):
    id: int
    name: str
    email: EmailStr | None
    status: str

    # ✅ Pydantic v2 way of enabling ORM support
    model_config = ConfigDict(from_attributes=True)


class PromoteRequest(BaseModel):
    value_cents: int
    seller_id: int | None = None
