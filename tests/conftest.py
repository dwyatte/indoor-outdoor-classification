import os
import pytest

@pytest.fixture()
def filename():
    return os.path.join(os.path.dirname(__file__), 'indoor.png')

