import os  
import numpy as np 
import cv2 
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Input, Dense 
from tensorflow.keras.models import Model

is_init = False
size = -1

label = []
dictionary = {}
c = 0

for i in os.listdir():
    if i.split(".")[-1] == "npy" and not(i.split(".")[0] == "labels"):  
        if not(is_init):
            is_init = True 
            X = np.load(i)
            size = X.shape[0]
            y = np.array([i.split('.')[0]]*size).reshape(-1,1)
        else:
            X = np.concatenate((X, np.load(i)))
            y = np.concatenate((y, np.array([i.split('.')[0]]*size).reshape(-1,1)))

        label.append(i.split('.')[0])
        dictionary[i.split('.')[0]] = c  
        c += 1

for i in range(y.shape[0]):
    y[i, 0] = dictionary[y[i, 0]]
y = np.array(y, dtype="int32")

# Convert labels to one-hot encoding
y = to_categorical(y)

# Shuffle data
combined = list(zip(X, y))  # Combine X and y into a list of tuples
np.random.shuffle(combined)  # Shuffle the combined list
X_new, y_new = zip(*combined)  # Unzip the shuffled list back into X_new and y_new
X_new = np.array(X_new)  # Convert X_new back to numpy array
y_new = np.array(y_new)  # Convert y_new back to numpy array


# Define model
ip = Input(shape=(X_new.shape[1],))  # Use X_new.shape instead of X.shape
m = Dense(512, activation="relu")(ip)
m = Dense(256, activation="relu")(m)
op = Dense(y_new.shape[1], activation="softmax")(m)  # Use y_new.shape instead of y.shape
model = Model(inputs=ip, outputs=op)

# Compile model
model.compile(optimizer='rmsprop', loss="categorical_crossentropy", metrics=['acc'])

# Train model
model.fit(X_new, y_new, epochs=50)

# Save model
model.save("model.h5")
np.save("labels.npy", np.array(label))