print('Hello There!')
import time
time.sleep(3)
print('How has you day been?')
txt = input("Type your answer here: ")

print(f"So your day was {txt}?")
time.sleep(1)
print("What is your name?")
name=input()
print(f"Ok {name}.")
time.sleep(1)
print("What year were you born?")
while True:
    try:
        # 👇️ use int() instead of float
        # if you only accept integers
        num = float(input())
        print(f"So you were born in {num}?")
        break
    except ValueError:
        print('Please enter a number.')


time.sleep(2)
print(f"Are you hungry {name}?")
answer = input("Enter yes or no: ") 
if answer == "yes": 
    print("So a yes!")
elif answer == "no": 
    print("So a no!")
else: 
    print("Please enter yes or no.") 



time.sleep(1)
print("Now that I have gathered your information I have a simple profile for you")
time.sleep(1)
print("Let me show you")
time.sleep(1)
print(f"So your name is {name} and you were born in {num}.")
time.sleep(5)
print("How are you feeling?")
input()
print("Hmmmm, I see")
time.sleep(3)
print("What state do you live in?")
state=input()
print(f"So you live in {state}")
time.sleep(2)
print("How old are you?")
age=input()
print(f"You are {age}!")
