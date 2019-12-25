import random
import time

#word_list = ['make', 'me', 'believe', 'again', 'in', 'some', 'kind', 'of', 'faith']

def hangman():
  start()
  words = []

  with open("words.txt", "r") as f:
      for line in f:
          words.extend(line.split())


  random.shuffle(words)

  word = list(words[0])

  #print(word)

  # empty list for guesses 
  guesses = []

  # contains guessedletters
  guessed = []

  #adds word to guesses
  guesses.extend(word)

  # adds what is inguesses toguessed so we can eliminate
  guessed.extend(guesses)

  # iterates through guesses
  for i in range(len(guesses)):
    #replaces each item with _
    guesses[i] = "_"

  #join puts space beween each _
  print(' '.join(guesses))
  print()

  #counter stops game when all letters are gessed
  count = 0

  incorrect = 7 #len(word)

  #keepsajing user tillworis guessed
  while count < len(guesses) and incorrect > 0:
    
    guess = input("Please guess a letter: ")
    guess = guess.lower()
    #print(count)

    # iterates throug letters in guessses
    for i in range(len(guesses)):
      # if guess matches letter
      if word[i] == guess and guess in guessed:
        # replace indexof that letter with actual letter
        guesses[i] = guess
        count += 1

        guessed.remove(guess)

    if guess not in word:
      incorrect -= 1
      print("Sorry, " + guess + " is not in the word")    
    print("You have guessed",count,"correct letters")
    print("You have:",incorrect,"chances left")


    # print new the new string
    print(' '.join(guesses))
    print()

  if count == len(word):
    print("AWESOME! You got it!")
  else:
    print("You lose")
    result = ''.join(str(e) for e in word)
    print("The word was: " + result)
   


def start():
  name = input("Please enter your name: ")
  print("Welcome",name,"Please wait...")
  time.sleep(2)
  print("Loading...")
  time.sleep(2)

hangman()

'''
play_again = True
while  play_again:
  word_list = ['make', 'me', 'believe', 'again']
  '''