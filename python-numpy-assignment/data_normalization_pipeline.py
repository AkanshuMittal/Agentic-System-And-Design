import numpy as np 

arr = np.array([10,20,30,40])

print(f"Original data: {arr}")

mean = np.mean(arr)

print(f"Mean: {mean}")

std = np.std(arr)

print(f"Standard Deviation: {std}")

normalized_arr = (arr - mean) / std

print(f"Normalized data: {normalized_arr}")

reshaped_arr = normalized_arr.reshape(2,2)

print(f"Reshaped normalized data: \n{reshaped_arr}")

print(f"Reshaped data shape: {reshaped_arr.shape}")