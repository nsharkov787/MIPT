from task6_sem3 import f
import numpy as np
x1 = [1, 2, 3]
y1 = [2, 4, 6]

x = np.array(x1)
y = np.array(y1)

result1 = f(x, y)

expect = 2

assert np.isclose(result1, expect), f"Тест 1 провален: ожидалось {expect}, получено {result1}"