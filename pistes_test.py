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


rand_03_03a = [0, 4, 3, 9, 8, 7, 6, 20, 17, 2, 5, 14, 15, 25, 13, 26, 11, 24, 21, 22, 18, 29, 23, 10, 12, 28, 16, 19, 27, 1]
rand_03_03b = [0, 24, 3, 28, 15, 19, 2, 17, 5, 4, 23, 27, 12, 13, 26, 14, 18, 22, 29, 16, 7, 20, 6, 1, 11, 8, 21, 10, 9, 25]
rand_03_03c = [0, 3, 23, 4, 14, 29, 1, 8, 9, 21, 5, 22, 19, 15, 25, 26, 27, 13, 12, 11, 7, 18, 17, 16, 6, 2, 10, 20, 28, 24]
hill_03_03a = [0, 3, 23, 4, 14, 29, 2, 8, 9, 21, 5, 22, 19, 15, 25, 26, 27, 13, 12, 11, 7, 18, 17, 16, 6, 10, 1, 20, 28, 24]
hill_03_03b = (0, 3, 14, 24, 15, 19, 21, 7, 8, 18, 2, 17, 5, 23, 27, 26, 12, 11, 4, 22, 29, 25, 10, 28, 20, 1, 6, 16, 9, 13)
hill_03_03c = [0, 3, 14, 4, 23, 17, 2, 7, 18, 21, 5, 22, 19, 15, 25, 13, 12, 26, 27, 11, 24, 9, 8, 16, 20, 6, 1, 29, 28, 10]
hill_03_03d = [0, 23, 4, 14, 3, 24, 11, 27, 26, 25, 15, 28, 19, 22, 5, 21, 17, 18, 7, 9, 8, 2, 16, 20, 6, 1, 29, 12, 13, 10]
hand_03_03a = [0, 23, 4, 14, 3, 24, 11, 27, 26, 25, 15, 19, 22, 5, 21, 17, 18, 7, 9, 8, 2, 16, 20, 6, 1, 29, 28, 12, 13, 10]
hill_03_03e = [0, 23, 4, 14, 3, 24, 11, 27, 26, 25, 15, 19, 22, 5, 21, 17, 2, 18, 7, 9, 8, 16, 20, 6, 1, 29, 28, 12, 13, 10]

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
  # Found by random search on 2017-03-03
  (rand_03_03a, 149084, coordinates),
  (rand_03_03b, 141621, coordinates),
  (rand_03_03c, 134941, coordinates),
  # Found by random hill climbing search on 2017-03-03
  (hill_03_03a, 126544, coordinates),
  (hill_03_03b, 118341, coordinates),
  # Found by exhaustive climbing search on 2017-03-03
  (hill_03_03c,  87313, coordinates),
  (hill_03_03d,  71953, coordinates),
  # Found by viewing graph of hill_03_03d and improving by hand
  # But the random + hill climb found it a bit later too
  (hand_03_03a,  70613, coordinates),
  # Hill climb finds a new champion
  (hill_03_03e,  70406, coordinates),
    ))
def test_total_wait_time(order, cost, positions):
    assert total_wait_time(order, positions) == cost
