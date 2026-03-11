# Writing to a new text file
file = open("dataset_log.txt", "w")
file.write("Epoch 1: 95% Accuracy\nEpoch 2: 97% Accuracy")
file.close()

# Reading the contents of the text file
file = open("dataset_log.txt", "r")
print("Reading File Contents:")
print(file.read())
file.close()



