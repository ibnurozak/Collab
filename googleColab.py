import numpy as np
input_features = np.array([[0,0],[0,1],[1,0],[1,1]])
print (input_features.shape)
input_features
target_output = np.array([[0,1,1,1]])
target_output = target_output.reshape(4,1)
print(target_output.shape)
target_output