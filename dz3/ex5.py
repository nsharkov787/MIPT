import pandas as pd
import matplotlib.pyplot as plt
r = pd.read_csv('BTC_data.csv')
x = list(r['time'])
y = list(r['close'])
plt.plot(x, y)
plt.savefig("биткоин")
plt.show()