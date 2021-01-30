from numpy import random
#ความหน้าจะเป็นในการกินข้าว2ครั้งจะมากกว่า2ครั้งหรือไม่
x = random.poisson(lam=2,size=10)
print(x)