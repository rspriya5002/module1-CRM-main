# tests/integration/test_leads_api.py
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

client = TestClient(app)

def setup_function():
    """Create tables before each test"""
    Base.metadata.create_all(bind=engine)

def teardown_function():
    """Drop tables after each test"""
    Base.metadata.drop_all(bind=engine)

def test_create_and_promote():
    # Step 1: Create a lead
    lead_data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    response = client.post("/leads/", json=lead_data)
    assert response.status_code == 201
    lead = response.json()
    assert "id" in lead
    lead_id = lead["id"]

    # Step 2: Promote lead to deal
    promote_data = {
        "value_cents": 50000  # Example deal value
    }
    response = client.post(f"/leads/{lead_id}/promote", json=promote_data)
    assert response.status_code == 201
    deal = response.json()

    # Step 3: Assert the response contains "deal_id"
    assert "deal_id" in deal
