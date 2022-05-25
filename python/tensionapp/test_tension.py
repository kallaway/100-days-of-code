import pytest
from model import Tracker, Medicament, Taker

def test_add_measure_to_tracker():
    first_measure = Tracker(1,"me", 120, 80, 70, "digital", "2022-01-10 08:00:00", "after breakfast", True, "Enalapril", "2022-01-09 21:00:00")
    second_measure = Tracker(2, "nurse", 130, 90, 60, "analogic", "2022-01-14 09:00:00", False)

    assert first_measure.id == 1
    assert second_measure.sys == 130
    assert second_measure.observation == ""
    assert first_measure
