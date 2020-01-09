import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.widgets import Slider

data = pd.read_csv('Climat.csv')
data2 = pd.read_csv('ClimatErreur.csv')

figzoom, axzoom = plt.subplots()
array = []
for col in data :
    array = [*array, *data[col].dropna()]   


array2 = []
for col in data2 :
    array2 = [*array2, *data2[col].dropna()]   

plt.plot(array)
plt.plot(array2)


plt.subplots_adjust(left=0.25, bottom=0.25)
plt.xlabel('Jour')
plt.ylabel('Température (°C)')

axzoom.set(xlim=(1, 31), autoscale_on=False,title='Zoom window')
axcolor = 'lightgoldenrodyellow'
axX = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
sX = Slider(axX, 'Freq', 1, 365, valinit=15, valstep=1)

def update(val):
    index = val
    min = int(val - 15)
    max = int(val + 15)
    if min < 1:
        min = 1
    if max > 365:
        max = 365
    axzoom.set_xlim(min,max)


sX.on_changed(update)

plt.legend()
plt.show()
