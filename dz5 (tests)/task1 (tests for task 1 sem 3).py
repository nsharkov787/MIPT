from task2_sem3 import f
assert f(360) == [2, 2, 2, 3, 3, 5]
assert f(-12) == [-1, 2, 2, 3]
assert f(1) == []
assert f(0) == [0]
assert f(97) == [97]
assert f(1000000) == [2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5]