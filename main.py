import random
import hangman_pics
import words

# Choose a random word from word list
chosen_word = random.choice(words.word_list)
game = []
for char in chosen_word:
  game.append("_ ")

# Start game
print("Welcome to Hangman.")
print(hangman_pics.pics[0])
print(''.join(game)+'\n')

max_wrong = 6
num_wrong = 0
remaining = len(game)
guesses = []
while num_wrong < max_wrong and remaining > 0:
  
  # Get user input
  guessed_letter = input("Guess a letter:\t").lower()

  # Add letter to guess list
  if guessed_letter not in guesses:
    guesses.append(guessed_letter)
    guesses.sort()

    # Correct guess
    if guessed_letter in chosen_word:
      # Subtract remaining
      remaining -= chosen_word.count(guessed_letter)
      
      # Replace with correct letter
      for i in range(0, len(chosen_word)):
        if chosen_word[i] == guessed_letter:
          game[i] = guessed_letter
      print(''.join(game)+'\n')

    # Incorrect guess
    else:
      num_wrong+=1
      print("Incorrect!")
      # Draw hangman
      print(hangman_pics.pics[num_wrong])
      # Print guesses
      print(f"{max_wrong - num_wrong} guesses remaining.")
      print(f"Guessed letters: {guesses}")

if remaining == 0:
  print("You win!")
else:
  print("You lose.")