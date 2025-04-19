import random
import mensagens
import clear_screen

def guess_the_number():
    number = random.randint(1, 300)
    guess = None
    level = input("Choose difficulty level (easy, hard): ").lower()

    if level not in ['easy', 'hard']:
        print("Invalid difficulty level. Please choose 'easy' or 'hard'.")
        return
    
    chances = 10 if level == "easy" else 5

    while guess != number and chances > 0:
        try:
            guess = int(input("Guess a number between 1 and 300: "))
            if guess < 1 or guess > 300:
                print("Invalid number. Please enter a number between 1 and 300.")
                continue 

            if guess > number:
                chances -= 1
                print("Too high! Try again. Chances left:", chances)
            elif guess < number:
                chances -= 1
                print("Too low! Try again. Chances left:", chances)
            else:
                print("🎉 Congratulations! You've guessed the number!")
                return
        except ValueError:
            print("Please enter a valid number.")
            
    clear_screen.clear_screen()
    mensagens.mensagem(f"\n Sorry, you've run out of chances. The number was: {number}\t ;-;")

        
    return number
    