
import json
from base.functions import *
from base.get_intention import get_intention

# open the json data file
with open("data/intents.json") as file:
    data = json.load(file)


def chat():
    # check if started
    print("start")
    # define the default user name
    name = "You"
    # check if awake
    awake = False

    while True:
        # show username
        inp = input(name + ": ")

        # get action tag
        tag = get_intention(inp)

        # check if not unknown
        if tag != "Unknown":

            # loop through intents
            for tg in data["intents"]:

                # check if the tag is the right one
                if tg["tag"] == tag:

                    # check if action is exiting
                    if tag == "exit":
                        # exit the loop
                        return

                    # check if awake
                    elif awake:

                        # check if changing name
                        if tag == "getting_name_rnd":
                            name = get_name(tg, inp, name)

                        # execute the right function
                        else:
                            exec(tg["function"] + "(tg, inp, name)")

                    # if not awake
                    else:
                        # check if trying to wake
                        if tag == "waking":
                            # wake up
                            awake = True
                            wake = tg["wakes"]
                            say(random.choice(wake))
                        else:
                            pass

        # unknown command
        else:
            if awake:
                say("I don't know how to do that.")
            else:
                pass


if __name__ == "__main__":
    chat()
