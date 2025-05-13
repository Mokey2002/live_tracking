# tests/unit/test_utils.py
from app.services.haversine import haversine

def test_haversine_distance():
    d = haversine(0, 0, 0, 1)  # ~111 km at equator
    assert round(d) == 111319

