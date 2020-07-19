###Module 03: Live Session Exercise: Exception Handling###
## Kip McCharen (cam7cu)
import os 
import time
import random

def interact_with_user():
    """Function to interact positively with the user, and call the doerrors() function.
        At random chance, a randomized encouragement string is added after each error from an iterator of short sentences. """
    #Create variables and data to function correctly
    encouragement = ["Hang in there.", "Don’t give up.", "Keep pushing.", "Keep fighting!", "Stay strong.", "Never give up.", "Never say ‘die’.", "You can do it!", "Follow your dreams.", "Reach for the stars.", "Do the impossible.", "Always believe in yourself.", "The sky is the limit."]
    random.shuffle(encouragement)
    encouragement = iter([x.lower().strip() for x in encouragement])
    args = [r"'2'+2", r"int('xyz')", r"x=100/0", r"open('madeupfile.txt')", r"os.remove(filepath)", "2.718281 ** 1000", "print 'whoooo'"]
    yourname = input("Hi there, what's your name?    -> ")
    yourname = "Gerethy"
    print(f"great! J/K I'm a computer not a person. I'll just call you {yourname}.")
    time.sleep(2)
    print(f"OK {yourname}, let's test some errors here.")
    time.sleep(2)
    for a in args:
        if bool(random.getrandbits(1)):
            doerrors(a, yourname, next(encouragement))
        else:
            doerrors(a)
    time.sleep(2)
    print(f"Well {yourname}, successfully produced errors! Is that a success or not?")
    time.sleep(3)
    print(f"Honestly, who's to say. Thanks for your help anyways. Don't forget, {next(encouragement)}")

def doerrors(a, yourname="", encouragement=""):
    """Function to handle errors correction from arguments passed in as text. Username and encouragement text accepted. """
    filepath = os.path.dirname(os.path.abspath(__file__))
    erout = lambda x,y: print(f"\tFailed to execute: {x}\n{type(err).__name__}: {y}")
    try:
        exec(a)
    except TypeError as err:
        erout(a,err)
    except ValueError as err:
        erout(a,err)
    except ZeroDivisionError as err:
        erout(a,err)
    except FileNotFoundError as err: 
        erout(a,err)
    except IOError as err: 
        erout(a,err)
    except ArithmeticError as err:
        erout(a,err)
    except Exception as err:
        erout(a,err)
    finally:
        if yourname != "" and encouragement != "":
            print(f"\t{yourname}, {encouragement}")
        else:
            print("\tRotten luck.")
        print("\n")
        time.sleep(2)

interact_with_user()