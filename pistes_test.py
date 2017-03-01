from pistes import coordinates


def test_30_coordinates():
    assert len(coordinates) == 30

def test_coordinates_in_range():
    x, y = zip(*coordinates)
    assert min(x) == -855
    assert max(x) ==  725
    assert min(y) == -655
    assert max(y) ==  515

def test_start_at_origin():
    assert coordinates[0] == (0,0)
    for p in coordinates[1:]:
        assert p != (0,0)
