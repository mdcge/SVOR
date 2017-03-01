from pytest import mark
parametrize = mark.parametrize

from pistes import (coordinates, distance, total_wait_time)


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



@parametrize('a b d'.split(),
   ((( 0, 0), ( 0, 1), 1),
    (( 0, 0), ( 3, 4), 5),
    (( 1, 1), ( 4, 5), 5),
    ((-1,-1), (-4,-5), 5),
))
def test_distance(a, b, d):
    assert distance(a,b) == d


_2_3_swap = list(range(30))
_2_3_swap[1], _2_3_swap[2] = _2_3_swap[2], _2_3_swap[1]


_swap_end = list(range(30))
_swap_end[-1], _swap_end[-2] = _swap_end[-2], _swap_end[-1]


@parametrize('order cost positions'.split(),
    (
  # One step of length 1, cost: 1
  ((0,1),     1, ((0,0), (0,1))),
  # Two steps of length 1 each, cost: 1+2 = 3
  ((0,1,2),   3, ((0,0), (0,1), (0,2))),
  # Three steps of lenth 1 each, cost: 1+2+3 = 6
  ((0,1,2,3), 6, ((0,0), (0,1), (0,2), (0,3))),
  # As above, but with a bend
  ((0,1,2,3), 6, ((0,0), (0,1), (1,1), (2,1))),
  # Taken from spreadsheet: in order
  (range(30), 212125, coordinates),
  # Taken from spreadsheet: 2nd and 3rd swapped
  (_2_3_swap, 211470, coordinates),
  # Taken from spreadsheet: last two swapped
  (_swap_end, 212572, coordinates),
    ))
def test_total_wait_time(order, cost, positions):
    assert total_wait_time(order, positions) == cost
