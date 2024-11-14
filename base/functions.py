import random
import datetime
import calendar
import webbrowser
import pytz
import pyautogui
import wikipedia
import requests
import subprocess


def say(phrase):
    print("Albert: " + phrase)


def greet(rnd, *_vars):
    greeting = rnd["greetings"]
    say(random.choice(greeting))


def mood_status(rnd, *_vars):
    mood = rnd["mood_statuses"]
    say(random.choice(mood))


def name_declarations(rnd, *_vars):
    my_name = rnd["name_declarations"]
    say(random.choice(my_name))


def get_name(_rnd, input_data, name, *_vars):  # unknown
    if "is " in input_data:
        a, b = input_data.split(" is ")
        name_output = b
        if name == name_output:
            say(random.choice(["you already told me", "i already know that"]))
        else:
            name = name_output
            say("nice to meet you " + name)

    elif "non " in input_data or "i don" in input_data or input_data == "":
        say("alright")

    else:
        if name == input_data:  # known
            say(random.choice(["you already told me", "i already know that"]))
        else:
            name = input_data
            say("nice to meet you " + name)

    return name


def tell_name(_rnd, _input_data, name, *_vars):
    say(name)


def time(_rnd, input_data, *_vars):
    date_time = datetime.datetime
    location = "Africa/Casablanca"
    a, b = input_data.split(" time")
    if b == "":
        pass
    else:
        c, d = b.split(" in ")
        location = d

    time_zone = pytz.timezone(location)
    datetime_tz = date_time.now(time_zone)
    time_sequence = ["It's %H, %M minutes and %S seconds", "%H:%M:%S"]
    say(datetime_tz.strftime(random.choice(time_sequence)))


def date(*_vars):
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]  # exp. friday
    month_num = now.month
    day_num = now.day
    # a list of months
    month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                  'October', 'November', 'December']
    # a list of ordinal numbers
    ordinal_numbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th',
                       '13st', '14nd', '15rd', '16th', '17th', '18th', '19th', '20th', '20th', '21st', '22nd',
                       '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    date_sequence = ['today is ' + weekday + ' ' + month_name[month_num - 1] + ' the ' + ordinal_numbers[day_num - 1],
                     "it's " + weekday + ' the ' + ordinal_numbers[day_num - 1] + ' of ' + month_name[month_num - 1]]
    say(random.choice(date_sequence))


def search_the_web(rnd, input_data, *_vars):
    a, b = input_data.split(" for ")
    search_term = b.replace(" ", "+")
    url = "https://duckduckgo.com/?q=" + search_term
    webbrowser.get().open(url)
    results = [str(random.choice(rnd["web_results"])), "Here is what I found for" + " ' " + b + " ' ",
               "here are the results for" + " ' " + b + " ' "]
    say(random.choice(results))


def search_youtube(rnd, input_data, *_vars):
    a, b = input_data.split(" for ")
    search_term = b.replace(" ", "+")
    url = "https://www.youtube.com/results?search_query=" + search_term
    webbrowser.get().open(url)
    results = [str(random.choice(rnd["youtube_results"])), "Here is what I found for" + " ' " + b + " ' ",
               "here are the results for" + " ' " + b + " ' "]
    say(random.choice(results))


def open_app(rnd, input_data, *_vars):
    a, b = input_data.split("pen")
    app = b

    for i in app:
        if i == "r":  # browser/firefox
            path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            subprocess.call([path])
            break
        elif i == "y":  # youtube
            url = "https://www.youtube.com"
            webbrowser.get().open(url)
            break
        elif i == "s":  # webtoons
            url = "https://www.webtoons.com"
            webbrowser.get().open(url)
            break
        else:
            pass

    answers = rnd["confirmations"]
    say(random.choice(answers))


def get_stock_price(rnd, input_data, *_vars):
    a, b = input_data.split(" of ")
    search_term = b.replace(" ", "+")
    url = "https://www.amazon.co.uk/s?k=" + search_term
    webbrowser.get().open(url)
    results = [rnd["price_results"], "Here is what I found for" + " ' " + b + " ' ",
               "here are the results for" + " ' " + b + " ' "]
    say(random.choice(results))


def weather(_rnd, input_data, *_vars):
    api_key = '0e92bdd4760ac6fe79924eeeba9b1d89'
    celsius = 'metric'
    city = 'Ahfir, MA'
    a, b = input_data.split(" weather")
    if b == "":
        pass
    else:
        c, d = b.split(" in ")
        city = d

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units={celsius}&APPID={api_key}'
    response = requests.get(url).json()

    # City
    print("city : " + str(response.get('name')))
    # Description
    print("status : " + str(response['weather'][0].get('description')))
    # Temp
    print("temperature :" + str(response['main'].get('temp')) + " °C")
    # Wind
    print("wind speed :" + str(response['wind'].get('speed')) + " m/s")


def rock_paper_scissors(rnd, _input_data, name, *_vars):
    say("alright. Choose among rock, paper or scissor")
    p_move = input(name + ": ")
    c_move = ""

    for i in p_move:
        if i == "k":
            c_move = "paper"
            break
        elif i == "p":
            c_move = "scissor"
            break
        elif i == "s":
            c_move = "rock"
            break

    say("I chose " + c_move + " and You chose " + p_move)
    brag = rnd["brags"]
    say(random.choice(brag))


def toss_a_coin(*_vars):
    moves = ["heads", "tails"]
    say(random.choice(moves))


def screenshot(rnd, _input_data, *_vars):
    screenshot_taken = pyautogui.screenshot()
    screenshot_taken.save("C:/Users/SEK171/Pictures/screenshots/screen.png")
    answers = rnd["confirmations"]
    say(random.choice(answers))


def search_for_definition(_rnd, input_data, *_vars):
    a, b = input_data.split(" of ")
    search_term = b.replace(" ", "+")
    definition = wikipedia.summary(search_term, sentences=2)
    say(definition)


def search_for_a_person(_rnd, input_data, *_vars):
    a, b = input_data.split(" is ")
    search_term = b.replace(" ", "+")
    person = wikipedia.summary(search_term, sentences=2)
    say(person)
