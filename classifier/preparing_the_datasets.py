import nltk
import json
import pickle
import numpy as np
from nltk.stem.lancaster import LancasterStemmer

# used to simplify the words to the bare minimum
stemmer = LancasterStemmer()

# open the data json file
with open("data/intents.json") as file:
    data = json.load(file)


def create_the_datasets():
    # create the data lists
    words = []
    labels = []
    docs_x = []
    docs_y = []

    # loop through the intents
    for intent in data["intents"]:
        # loop through the patterns
        for pattern in intent["patterns"]:
            # get all the words separately
            pattern_words = nltk.word_tokenize(pattern)
            # put all the words in the words list
            words.extend(pattern_words)
            # add the pattern to the docs
            docs_x.append(pattern_words)
            # add the tag of the intent to the docs
            docs_y.append(intent["tag"])

            # if the tag is not a label
            if intent["tag"] not in labels:
                # put it inside it
                labels.append(intent["tag"])

    # stem all the words
    words = [stemmer.stem(w.lower()) for w in words if w != "?" and w != "!"]
    # remove the duplicates and sort the words
    words = sorted(list(set(words)))

    # sort all the labels
    labels = sorted(labels)

    # make training and output lists ( one hot encoded )
    training = []
    output = []

    # make an output list of 0 for all labels except for the ones we need
    out_empty = [0 for _ in range(len(labels))]

    # loop through the patterns
    for x, doc in enumerate(docs_x):
        # create the bag of words
        bag = []

        # stem all the words in the pattern
        pattern_words = [stemmer.stem(w.lower()) for w in doc]

        # loop through the stemmed words
        for w in words:
            # if the word is from the pattern append a 1
            if w in pattern_words:
                bag.append(1)
            # else append a 0
            else:
                bag.append(0)

        # check where the current tag exists on the labels list
        output_row = out_empty[:]
        # set the tag to 1
        output_row[labels.index(docs_y[x])] = 1

        # add the bag to the training list
        training.append(bag)
        # add the output row to the output
        output.append(output_row)

    # turn the lists into numpy arrays
    training = np.array(training)
    output = np.array(output)

    # save the model data
    with open("classifier/model_data.pickle", "wb") as f:
        pickle.dump((training, output), f)

    # save the main data
    with open("data/main_data.pickle", "wb") as f:
        pickle.dump((words, labels), f)


if __name__ == "__main__":
    # create the datasets
    create_the_datasets()
