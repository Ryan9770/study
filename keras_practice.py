import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
import tensorflow as tf;
from tensorflow import keras
from keras import layers
from keras.utils import plot_model

#
#           O        O  
#   O       O        O
#   O       O        O       O
#   O       O        O 
#           O        O
# input hidden1   hidden2  output
#
inputs = keras.Input(shape=(784,)) # input layer 784개 생성 

img_input = keras.Input(shape=(32,32,3)) # input layer 32*32*3 형태의 3차원 레이어 생성

print(inputs.shape)

print(inputs.dtype)

dense = layers.Dense(64, activation="relu")
x = dense(inputs)
x = layers.Dense(64, activation="relu")(x)
outputs = layers.Dense(10)(x)
model = keras.Model(inputs=inputs, outputs=outputs, name="model1")

model.summary()

#graphviz 문제로 사용 불가
#keras.utils.plot_model(model, "model1.png")

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train = x_train.reshape(60000, 784).astype("float32") / 255
x_test = x_test.reshape(10000, 784).astype("float32") / 255

model.compile(
    loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=keras.optimizers.RMSprop(),
    metrics=["accuracy"],
)

history = model.fit(x_train, y_train, batch_size=31, epochs=2, validation_split=0.2)

test_scores = model.evaluate(x_test, y_test, verbose=2)
print("loss : ", test_scores[0])
print("accuracy", test_scores[1])

model.save("path_to_first_model")

del model

model = keras.models.load_model("path_to_first_model")
