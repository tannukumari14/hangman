# import string
# from words import choose_word
# from image import IMAGES

# def ifvalid(user_input):
#   if len(user_input)!=1:
#     return False
  
#   if not user_input.isalpha():
#     return False
#   return True

# def word_guessed(secret_word, letters_guessed):
#   if secret_word==get_guessed_word(secret_word,letters_guessed):
#     return True
#   return False

# def get_guessed_word(secret_word,letters_guessed):
      

#   index = 0
#   guessed_word = ""
#   while (index < len(secret_word)):
#     if secret_word[index] in letters_guessed:
#       guessed_word += secret_word[index]
#     else:
#       guessed_word += "_"
#     index += 1

#   return guessed_word


def get_available_letters(letters_guessed):
      
  import string
  letters_left = string.ascii_lowercase
  letters_left=" "
  for letters in letters_left:
    if letters not in letters_guessed:
      letters_left+=letters


    return letters_left
def get_hint(secret_word,letters_guessed):
  import random
  letters_not_guessed=[]
  for i in secret_word:
    if i  not in  letters_guessed:
      if i not in letters_not_guessed:
        letters_not_guessed.append(i)
  return random.choice(letters_not_guessed)

def hangman(secret_word):
  print ("Welcome to the game, Hangman!")
  print ("I am thinking of a word that is "+str(len(secret_word))+ " letters long.")
  print ("")
  total_lives=remaining_lives=8
  image_selection=[0,1,2,3,4,5,6,7]
  level=input("enter the level in which you want to play""\n""a for easy""\n""b for medium""\n""c for hard level")
  if level not in ["a","b","c"]:
    print("aapki choice invalid hai .\n game easy mode mei start kar rahe hai")
  else:
    if level=="b":
      total_lives=remaining_lives=6
      image_selection=[1,2,3,4,5,6,7]
    elif level=="c":
      total_lives=remaining_lives=4
      image_selection=[1,3,5,7]
    elif level!="a":
      total_lives=remaining_lives=8
      images_selection=[1,2,3,4,5,6,7]
  letters_guessed=[]
  while(remaining_lives>0):
    available_letters = get_available_letters(letters_guessed)
    print ("Available letters:" + available_letters)
    guess = input("Please guess a letter: ")
    letter = guess.lower()
    if letter=="hint":
      print("your hint for this secret word is")+get_hint(secret_word,letters_guessed)
    elif (not ifvalid(letter)):
      print("invalid input",guess)
      continue

    elif letter in secret_word:
      letters_guessed.append(letter)
      print(letters_guessed)
      print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
      print ("")
      
    else:
        print ("Oops! That letter is not in my word: "+ get_guessed_word(secret_word, letters_guessed))
        print (IMAGES[image_selection[total_lives-remaining_lives]])
        remaining_lives-=1
        letters_guessed.append(letter)
        print("remaining_lives:"+str(remaining_lives))
        print ("")
        letters_guessed.append(letter)
        if word_guessed(secret_word,letters_guessed)==letters_guessed:
          print("**congrautulation ,you won**")
          print("")
  else:
    print("sorry you lose the game,the word was" +str(secret_word)+" . ")
secret_word=choose_word()
hangman(secret_word)