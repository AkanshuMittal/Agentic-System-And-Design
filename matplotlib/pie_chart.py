import matplotlib.pyplot as plt

# Data (example)
labels = ['Correct', 'Incorrect', 'Not Detected']
values = [70, 20, 10]


plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Cheque OCR Performance")

plt.show()