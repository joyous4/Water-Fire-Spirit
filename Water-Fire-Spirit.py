import random  # importing random module
import pyttsx3  # after installing pyttsx3 module we are importing it
import speech_recognition as s

speech = pyttsx3.init()  # initializing the speech
speech.setProperty('rate', 200)  # Seting speed percent and volume
speech.setProperty('volume', 1)

print("Welcome to Water Fire Spirit Game.")  # introduction to the game
speech.say("Welcome to Water-Fire-Spirit Game")
speech.runAndWait()

print("\nRules of the game are given as below :\n1."
      "Spirit controls water.\n2.Water puts out fire.\n3.Fire scares spirit.")  # rules of the game
speech.say("Rules of the game")
speech.say("Spirit controls water")
speech.say("Water puts out Fire")
speech.say("Fire scares spirit")
speech.runAndWait()

print("\nTell your choice : Water/Fire/Spirit : ")  # commanding for user input
speech.say("Tell your choice ")
speech.say("water fire spirit")
speech.runAndWait()

sr = s.Recognizer()     # voice recognition for user input
print("(tell now:)")
with s.Microphone() as m:
    audio = sr.listen(m)
    user = sr.recognize_google(audio, language='eng-in')
    print(user)

possible_actions = ["water", "fire", " spirit"]   # making the computer choose
comp = random.choice(possible_actions)  # this allows to randomly select element from the list


show = f"You chose {user}, computer chose {comp} "  # showing the output of the user and the computer chosen value
print(show)
speech.say(show)

if user == comp:            # when the user and the computer chooses same symbol
    print("It's a tie ! ")
    speech.say("It's a tie !")

elif user == "water":       # when the user chooses water
    if comp == "fire":
        print("Water puts out fire. Congrats you won ! ")
        speech.say("Water puts out fire")
        speech.say("Congrats you won")
    elif comp == "spirit":
        print("Spirit controls water. Better luck next time.")
        speech.say("Spirit controls water")
        speech.say("Better luck next time")

elif user == "fire":       # when the user chooses fire
    if comp == "water":
        print("Water puts out fire. Better luck next time. ")
        speech.say("Water puts out fire")
        speech.say("Better luck next time")
    elif comp == "spirit":
        print("Fire scares spirit. Congrats you won ! ")
        speech.say("Fire scares spirit")
        speech.say("Congrats you won ")

elif user == "spirit":       # when the user chooses spirit
    if comp == "fire":
        print("Fire scares spirit. Better luck next time. ")
        speech.say("Fire scares spirit")
        speech.say("Better luck next time ")
    elif comp == "water":
        print("Spirit controls water.Congrats you won !")
        speech.say("Spirit controls water")
        speech.say("Congrats you won !")
else:
    print("\nInvalid input.\nPlease tell water/fire/spirit next time.")
    speech.say("Invalid input")
    speech.say("Please tell water or fire or spirit next time.")

speech.runAndWait()
