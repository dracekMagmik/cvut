import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.,5.,0.1)
print(x)
y = np.sin(x)
print(y)
plt.plot(x,y)
plt.show()
plt.xlabel('osa x')
plt.ylabel('osa y')
#ten obrayek idealně uloyit jako pdf nebo eps(?), pak to bude vektorový a bude s tím požnost dělat co chci :)
