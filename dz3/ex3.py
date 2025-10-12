import pandas as pd
import matplotlib.pyplot as plt
data = list(pd.read_csv('iris_data.csv')['PetalLengthCm'])
a = len([x for x in data if x < 1.2])/len(data)
b = len([x for x in data if 1.2 <= x < 1.5])/len(data)
c = len([x for x in data if x >= 1.5])/len(data)
plt.pie([a, b, c], labels=["x<1.2", "1.2<=x<1.5", "x>=1.5"])
plt.title("IRIS")
plt.savefig('iris.png')
plt.show()
