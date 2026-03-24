import numpy as np 
import matplotlib.pyplot as plt

epochs = np.arange(1,11)
#print(epochs)

loss = np.linspace(1.0, 0.3, 10)
print(loss)

# Line Plot
plt.figure(figsize=(8,5))
plt.plot(epochs, loss, marker='o')
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Training Loss vs Epoch")
plt.grid(True)

plt.show()