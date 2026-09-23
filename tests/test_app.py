import sys
from pathlib import Path

# Allow importing app.py from the app folder
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from app import (
    calculate_recommended_quantity,
    calculate_surplus,
    classify_demand,
)


def test_calculate_recommended_quantity():
    result = calculate_recommended_quantity(100, 10)
    assert result == 110


def test_calculate_surplus():
    result = calculate_surplus(150, 100)
    assert result == 50


def test_calculate_shortage():
    result = calculate_surplus(80, 100)
    assert result == -20


def test_classify_low_demand():
    result = classify_demand(50, 100, 200)
    assert result == "Low"


def test_classify_medium_demand():
    result = classify_demand(150, 100, 200)
    assert result == "Medium"


def test_classify_high_demand():
    result = classify_demand(250, 100, 200)
    assert result == "High"