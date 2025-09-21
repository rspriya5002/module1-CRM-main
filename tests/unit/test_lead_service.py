from unittest.mock import MagicMock
from app.services.lead_service import LeadService

# Dummy lead class
class DummyLead:
    def __init__(self, id):
        self.id = id
        self.status = "new"

def test_promote_to_deal_success():
    # Arrange
    lead = DummyLead(123)

    lead_repo = MagicMock()
    lead_repo.get.return_value = lead

    deal_repo = MagicMock()
    deal_repo.create.return_value = {"id": 999}

    mock_session = MagicMock()
    mock_session.__enter__.return_value = mock_session  # context manager
    mock_session.__exit__.return_value = False

    service = LeadService(
        lead_repo=lead_repo,
        deal_repo=deal_repo,
        session_factory=lambda: mock_session  # inject mock session factory
    )

    # Act
    result = service.promote_to_deal(lead_id=123, value_cents=10000)

    # Assert
    lead_repo.get.assert_called_once_with(mock_session, 123)
    deal_repo.create.assert_called_once_with(mock_session, {"lead_id": 123, "value_cents": 10000, "seller_id": None})
    assert result == {"id": 999}
    assert lead.status == "promoted"
