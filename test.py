#! /usr/bin/env python

from best_route import best_route

assert best_route((
    (1,),
    (2, 3),
    (3, 3, 1),
    (3, 1, 5, 4),
    (3, 1, 3, 1, 3),
    (2, 2, 2, 2, 2, 2),
    (5, 6, 4, 5, 6, 4, 3)
)) == 23

assert best_route((
    (1,),
    (2, 1),
    (1, 2, 1),
    (1, 2, 1, 1),
    (1, 2, 1, 1, 1),
    (1, 2, 1, 1, 1, 1),
    (1, 2, 1, 1, 1, 1, 9)
)) == 15

assert best_route((
    (9,),
    (2, 2),
    (3, 3, 3),
    (4, 4, 4, 4)
)) == 18

assert best_route((
    (1,),
    (2, 9),
    (8, 8, 0),
    (4, 4, 4, 9)
)) == 22
