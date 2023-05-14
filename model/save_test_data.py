import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load the test data and labels
(_, _), (testX, testY) = mnist.load_data()

# Preprocess the test data
testX = np.expand_dims(testX, axis=-1)
testX = testX.astype("float32") / 255.0
testY = to_categorical(testY, 10)

# Save the test data and labels to a file
np.savez('mnist_test_data.npz', testX=testX, testY=testY)
