c = 6
d = 12
input("Welcome! Press enter to begin")
while True:
  print("\nLet me tell you about myself.")
  import time
  time.sleep(1)
  print("I'm just 109 lines of python.")
  import time
  time.sleep(1)
  print("But somehow, just like humans, I am still tired...")
  time.sleep(2)
  test = input("\nAre you also tired? (y/n)")
  if test == "y":
    print("\nSorry to hear that.")
    time.sleep(.5)
    break
  if test == "n":
    print("\nI'm glad to hear that.\nGood for you!")
    import time
    time.sleep(.5)
    print("Goodbye!")
    exit()
  else: 
    print("\nUm...\n")
    import time
    time.sleep(1)
    print("That doesn't quite answer my question. \n") 
    time.sleep(1)
    print("Could you rephrase?\n")
    time.sleep(1)

while True:
  fix = input("Can I try to help you fix it? (y/n)")
  if fix == "y":
    print("\nGreat, let's begin.")
    import time
    time.sleep (.5)
    break
  if fix == "n":
    import time
    time.sleep(.5)
    print("\nOh, well this awkard.")
    time.sleep(.5)
    print("Best of luck, I guess. Goodye.")
    exit()
  else: 
    print("Um...\n")
    import time
    time.sleep(1)
    print("That doesn't quite answer my question. \n") 
    time.sleep(1)
    print("Could you rephrase?\n")
    time.sleep(.5)

while True:
  value = input("\nHow many hours did you sleep last night?")
  hours = int(value)
  if hours <= c:
    print("\n")
    print("That's all?!?")
    import time
    time.sleep (.5)
    print("This is why you're tired, silly goose!")
    time.sleep(1)
    print("No worries. Just try to get some more sleep tonight. :)")
    time.sleep(1)
    break
  if hours < d:
    print("\nHm...")
    time.sleep(1)
    print("I'm not sure what the problem is then.")
    time.sleep(.5)
    print("I give up.")
    break
  if hours > d:
    print("\nPlease tell me that's a typo.")
    import time
    time.sleep(.5)
    print("Let's try again.\n")
  else:
    print("\nNumbers only, please!\n")

while True:
  import time
  time.sleep (1) 
  print("\nAnything else I can do for you?")
  time.sleep (.5)
  print("\nA. I'd love a sandwich.") 
  print("B. Nope, you've done enough. Good python. :)")
  final = input("\na or b?")
  if final == "a":
    print("\nMe too, but there's nothing I can do about it for either of us.")
    time.sleep(.5)
    print("Well...")
    time.sleep(1)
    print("Goodbye!")
    exit()
  if final == "b":
    print ("\nThanks :) goodbye!")
    exit()
  else:
    print("Um...\n")
    import time
    time.sleep(1)
    print("Think we might have had a misconnection here. \n") 
    time.sleep(1)
    print("Could you rephrase?\n")
    time.sleep(.5)
