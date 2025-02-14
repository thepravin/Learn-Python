
# binomial distribution - discrete distribution - binary output.

# parameters -> n = number of trials
#               p = probability
#               size = returned array


from numpy import random

x = random.binomial(n=10, p=0.5, size=10)
print(x)


# visulization of binomial distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True , kde=False)
plt.show()


# Difference between normal and binomial - normal (continues) and binomial (discreate)

# Use 500 datapoint (size) for binomial and under 100 datapoint for normal dist.