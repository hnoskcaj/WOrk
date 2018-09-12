import random
import math as m

theta = random.random()*m.pi*2
answer = m.sin(theta)**2 + m.cos(theta)**2
print(answer)