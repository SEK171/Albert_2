from tensorflow import keras
import numpy as np
import pickle
import json
import nltk
from nltk.stem.lancaster import LancasterStemmer

# used to simplify the words to the bare minimum
stemmer = LancasterStemmer()

# open the json data file
with open("data/intents.json") as file:
    data = json.load(file)

# open the main data
with open("data/main_data.pickle", "rb") as f:
    words, labels = pickle.load(f)

# initiate the model
model = keras.models.load_model("data/model.h5")


def bag_of_words(s, words_list):
    # store all the words
    bag = [0 for _ in range(len(words_list))]
    # get a list of tokenized words
    s_words = nltk.word_tokenize(s)
    # stem the words
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    # generate the list (bag)
    for se in s_words:
        for i, w in enumerate(words_list):
            if w == se:
                bag[i] = 1

    # return a numpy array with the bag
    return np.array([bag])


def get_intention(inp):

    intention = ""

    results = model.predict([bag_of_words(inp, words)])[0]
    results_index = np.argmax(results)
    tag = labels[results_index]
    if results[results_index] > 0.6:

        for tg in data["intents"]:
            if tg["tag"] == tag:
                intention = tag

    else:
        intention = "Unknown"

    return intention
