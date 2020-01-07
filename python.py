import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Climat.csv')
# print(data.shape)
#array = data.values

for col in data :    
    plt.plot(data[col], label=col)
plt.xlabel('Jour')
plt.ylabel('Température (°C)')
plt.legend()
plt.show()