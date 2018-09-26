import sys
n = [int(x)for x in str(sys.arv[1])]
answer = sum[(2**i)*n[i] for i in range(len(n))[::-1]]
print (answer)