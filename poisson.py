from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

"""
#ความหน้าจะเป็นในการกินข้าว2ครั้งจะมากกว่า2ครั้งหรือไม่
x = random.poisson(lam=2,size=10)
print(x)
"""

sns.displot(random.poisson(lam=2,size=100))
plt.show()