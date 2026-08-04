import sys
import pytest
from reader import validate_row

@python.fixtures
def sample_emp():
    return[
        [
            "ID_001",
            "Alexa James",
            "25",
            "Female",
            "Product",
            "0",
            "86241",
            "Yes",
            "8.93",
            "Chicago"
        ]
    ]

def validate_age(age):
    if age <= 0:
        raise ValueError("Invalid Age")
    return True

@pytest.fixture
def valid_age():
    return 25

def test_valid_age(valid_age):
    assert validate_age(valid_age)

def test_invalid_age():
    with pytest.raises(ValueError):
        validate_age(-25)