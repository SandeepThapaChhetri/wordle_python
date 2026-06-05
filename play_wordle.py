from wordle import Wordle

def main():
  print("Hello World!")
  wordle = Wordle("APPLE")
  
  while wordle.can_attempt:
    x = input("Type your guess:")
    wordle.attempts.append(x)
    if x == wordle.secret:
      print("You have guessed the word!")
      break
    print("Your guess is incorrect.")



if __name__ == "__main__":
  main()