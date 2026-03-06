import numpy as np

print("===== 1. DATA SAVING & LOADING =====")

# Create sample array
data = np.array([[10, 20, 30],
                 [40, 50, 60]])



np.savetxt("my_array.txt", data)


# Load array
loaded = np.loadtxt("my_array.txt").astype(np.int64)

print("Loaded Array:\n", loaded)





# Save array
# np.save("my_array.npy", data)

# Load array
# loaded = np.load("my_array.npy")

# print("Loaded Array:\n", loaded)






