import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./linearly_separable.csv')
df = pd.DataFrame(data, columns=['x', 'y', 'type'])
plt.scatter(0, 1, c=df['type'])
plt.show()
