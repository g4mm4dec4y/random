import time

def intro():
    print("\n\n*Applause*\nOh-ho ho ho-ho")
    time.sleep(3)
    print("Ha-ha ha")
    time.sleep(1)
    print("Wow... so tiny")
    time.sleep(3)
    print("Hello!")
    time.sleep(1)

def interrogation():
    print("Hello!")
    time.sleep(2)
    name = input("What is your name? ")
    time.sleep(0.5)
    age = input("How old are you? ")
    time.sleep(0.5)

    if age == "4 years old":
        time.sleep(0.5)
        print("\nYou are the youngest person EVER!\n")
        time.sleep(2)
    else:
        print("You are the oldest person EVER!")


intro()
interrogation()