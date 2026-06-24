import numpy as np

t = np.linspace(0,10,100)
soc = np.exp(-0.1*t)

print("Battery State of Charge Model")
print(soc)