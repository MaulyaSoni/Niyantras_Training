import sys
import pytest
from reader import AgeException, validate_row

@pytest.fixture
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

@pytest.fixture
def valid_age():
    return 25

def test_valid_age(sample_emp):
    assert validate_row(sample_emp[0]) is None

def test_invalid_age(sample_emp):
    sample_emp[0][2] = "-25"

    with pytest.raises(AgeException):
        validate_row(sample_emp[0])