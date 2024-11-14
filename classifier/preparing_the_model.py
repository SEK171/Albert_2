
import pickle
import tensorflow as tf
from tensorflow import keras

# open the model data
with open("classifier/model_data.pickle", "rb") as f:
    training, output = pickle.load(f)


def create_the_model():
    # reset the graph data
    tf.compat.v1.reset_default_graph()

    # define the keras model
    model = keras.Sequential()

    # input layer
    model.add(keras.layers.Dense(8, activation='relu', input_shape=(len(training[0]),)))
    # hidden layer
    model.add(keras.layers.Dense(8, activation="relu"))
    # output layer
    model.add(keras.layers.Dense(len(output[0]), activation="softmax"))

    # compile the model
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

    # fit and save the model
    model.fit(training, output, epochs=1000, batch_size=8)
    model.save("data/model.h5")


if __name__ == "__main__":
    # create the model
    create_the_model()
