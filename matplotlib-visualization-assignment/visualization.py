import numpy as np 
import matplotlib.pyplot as plt

epochs = np.arange(1,11)
#print(epochs)

loss = np.linspace(1.0, 0.3, 10)
#print(loss)

models = ['Model A', 'Model B', 'Model C']
accuracy = [0.85, 0.90, 0.88]

## Line Plot
plt.figure(figsize=(8,5))
plt.plot(epochs, loss, marker='o')
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Training Loss vs Epoch")
plt.grid(True)

plt.show()

## Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(epochs, loss)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Epoch vs Loss")

plt.show()

## Bar chart
plt.figure(figsize=(8,5))
plt.bar(models, accuracy)
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.title("Model Accuracy Comparison")

plt.show()

