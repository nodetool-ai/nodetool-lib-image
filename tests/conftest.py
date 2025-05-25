import pytest
from nodetool.workflows.processing_context import ProcessingContext


@pytest.fixture
def context():
    """Provide a ProcessingContext fixture for tests."""
    return ProcessingContext()