import sys
from pathlib import Path

import pytest
from nodetool.workflows.processing_context import ProcessingContext

# Ensure local sources are importable
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


@pytest.fixture
def context():
    """Provide a ProcessingContext fixture for tests."""
    return ProcessingContext()
