import nltk

import pickle

import random

import requests

from bs4 import BeautifulSoup

from nltk.tokenize import word_tokenize

from nltk.stem.lancaster import LancasterStemmer

import speech_recognition as sr

import pyttsx3

# Initialize the stemmer

stemmer = LancasterStemmer()

# Load the pre-trained intents and words from a file

with open('intents.pickle', 'rb') as file:

    intents = pickle.load(file)

with open('words.pickle', 'rb') as file:

    words = pickle.load(file)

# Load the trained model

with open('model.pickle', 'rb') as file:

    model = pickle.load(file)

# Initialize the speech recognizer and synthesizer

recognizer = sr.Recognizer()

synthesizer = pyttsx3.init()

# Define a function to preprocess the input sentence

def preprocess_sentence(sentence):

    tokens = word_tokenize(sentence.lower())

    tokens = [stemmer.stem(word) for word in tokens]

    return tokens

# Define a function to predict the intent based on the input sentence

def predict_intent(sentence):

    tokens = preprocess_sentence(sentence)

    bag = [0] * len(words)

    for w in tokens:

        for i, word in enumerate(words):

            if word == w:

                bag[i] = 1

    results = model.predict([bag])[0]

    results_index = numpy.argmax(results)

    intent = intents[results_index]

    return intent

# Define a function to generate a response based on the predicted intent

def generate_response(intent):

    for i in intents:

        if i['tag'] == intent:

            if 'action' in i:

                return perform_action(i['action'])

            else:

                return random.choice(i['responses'])

# Define a function to perform a specific action

def perform_action(action):

    if action == 'web_search':

        query = listen_input("What would you like to search for?")

        return search_web(query)

    elif action == 'play_game':

        return play_game()

    else:

        return "I'm sorry, I don't know how to perform that action."

# Define a function to listen to user's speech input

def listen_input(prompt):

    with sr.Microphone() as source:

        print(prompt)

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio)

        print("You:", text)

        return text

    except sr.UnknownValueError:

        return ""

    except sr.RequestError:

        return ""

# Define a function to speak the chatbot's response

def speak_response(response):

    print("Chatbot:", response)

    synthesizer.say(response)

    synthesizer.runAndWait()

# Define a function to play a number-guessing game

def play_game():

    target_number = random.randint(1, 100)

    speak_response("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    while True:

        user_guess = listen_input("Your guess:")

        try:

            guess = int(user_guess)

            if guess == target_number:

                return "Congratulations! You guessed the correct number."

            elif guess < target_number:

                speak_response("Try guessing a little higher.")

            else:

                speak_response("Try guessing a little lower.")

        except ValueError:

            speak_response("Sorry, I didn't understand your guess. Please try again.")

# Welcome message

speak_response("Welcome to the Chatbot! How can I assist you?")

# Main interaction loop

while True:

    user_input = listen_input("You:")

    if user_input.lower() == 'quit':

speak_response("Goodbye! Have a great day!")

break intent = predict_intent(user_input)

response = generate_response(intent)

speak_response(response)

 

