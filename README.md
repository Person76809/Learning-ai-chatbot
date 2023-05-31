# Learning-ai-chatbot
This code is for a chat bot that learns the more you teach it and talk to it

Respond to user inputs using natural language processing techniques.

Perform web searches based on user queries.

Scrape information from websites based on search queries.

Utilize speech recognition to listen to user speech input.

Synthesize speech to provide responses to the user.

Play a number-guessing game with the user.

Overall, the script functions as a chatbot that can understand and respond to user inputs, perform web searches, and engage in a simple game.


Importing Libraries: The script begins by importing the required libraries, including nltk for natural language processing, pickle for loading pre-trained models, random for generating random responses, requests for making HTTP requests, BeautifulSoup for web scraping, speech_recognition for speech recognition, and pyttsx3 for text-to-speech synthesis.

Initializing Components: The stemmer (LancasterStemmer) is initialized to perform stemming, which reduces words to their base or root form. Pre-trained intents and words are loaded from pickle files. The trained model is also loaded from a pickle file. The speech recognizer (Recognizer) and speech synthesizer (pyttsx3) are initialized for speech input and output.

Preprocessing Input: The preprocess_sentence() function tokenizes the input sentence into individual words, converts them to lowercase, and applies stemming. This preprocessing step helps in standardizing the input for better intent prediction.

Predicting Intent: The predict_intent() function takes a preprocessed sentence and predicts the intent using a bag-of-words approach. It creates a bag of words representation of the input sentence and feeds it to the pre-trained model. The model predicts the probabilities of different intents, and the intent with the highest probability is selected as the predicted intent.

Generating Response: The generate_response() function takes the predicted intent and generates a response based on the predefined intents. It searches for the matching intent in the loaded intents data and checks if there is a specific action associated with it. If an action is defined, it performs the corresponding action (such as web search or playing a game). If no action is defined, it randomly selects a response from the available responses.

Performing Actions: The script includes a perform_action() function that handles specific actions based on the action tag defined in the intents data. Currently, it supports two actions: 'web_search' and 'play_game'. For 'web_search', it prompts the user for a query, performs a web search, and returns the search results. For 'play_game', it initiates a number-guessing game, where the chatbot thinks of a number and the user tries to guess it.

Listening and Speaking: The listen_input() function utilizes the speech recognition library to listen to the user's speech input. It prompts the user with a given prompt and uses the microphone as the audio source. The audio is adjusted for ambient noise, and the recognizer attempts to transcribe the speech input using the Google Speech Recognition API.

Speaking the Response: The speak_response() function prints the chatbot's response and uses the speech synthesizer to convert the response into audible speech.

Main Interaction Loop: The script enters a while loop for the main interaction with the user. It listens to the user's input using listen_input(), predicts the intent using predict_intent(), generates a response using generate_response(), and speaks the response using speak_response(). The loop continues until the user enters 'quit' as their input, at which point the chatbot says goodbye and the loop breaks, terminating the script 
