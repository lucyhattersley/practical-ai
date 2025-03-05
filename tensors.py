import numpy as np
import tensorflow as tf

# Creating a 1D tensor (vector)
vector = np.array([1, 2, 3])
print(vector.shape)  # Output: (3,)

# Creating a 2D tensor (matrix)
matrix = np.array([[1, 2], [3, 4]])
print(matrix.shape)  # Output: (2, 2)

# Creating a 3D tensor (e.g., image with 3 color channels)
image_tensor = tf.random.uniform(shape=[64, 64, 3])
print(image_tensor.shape)  # Output: (64, 64, 3)