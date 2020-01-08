import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Climat.csv')
# print(data.shape)
#array = data.values
print("moyenne")
print(data.mean())
print("min")
print(data.min())
print("max")
print(data.max())
print("Ecart type")
print(data.std())



for col in data :    
    plt.plot(data[col].dropna(), label=col)
plt.xlabel('Jour')
plt.ylabel('Température (°C)')
plt.legend()
plt.show()

array = []
for col in data :
    array = [*array, *data[col].dropna()]   
plt.plot(array)
plt.xlabel('Jour')
plt.ylabel('Température (°C)')
plt.legend()
plt.show()