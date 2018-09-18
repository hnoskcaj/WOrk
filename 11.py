import sys
import numpy as np
a = np.greater_equal([4.85, 4.7, 4.5, 4.2, 3.85, 3.5, 3.2, 2.85, 2.5, 2, 1.5, 1, 0],[sys.argv[1]])
mask = sys.argv[1] >= a
mask2 = sys.argv[1] < a
b = 