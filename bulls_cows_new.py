import random
import time
start = time.time()


# Greet the user
print('Hi there!')
print("I've generated a random 4 digit number for you. Let's play a bulls and cows game.")


# Randomly choose winning number
def play(number_digits):
    # generate list of random integers of length number_digits (4 digits)
    key_game = [random.randint(0, 9) for n in range(number_digits)]
    print("Key for game: ", str(key_game))

    count = 0
    start = time.time()
    while True:
        count += 1
        print('Guess: ', count)
        print('Please enter the 4-digit number: ')
        guess_number = [int(i) for i in str(input())]

        if guess_number == key_game:
            end = time.time()
            print('Excellent, you have guessed the number!')
            print('It took you', count, 'guess(es)!')
            duration = round(end - start, 2)
            print("Reaction Time: " + str(duration) + " seconds.")
            break

        else:
            cows = 0
            bulls = 0

            for n in range(0, number_digits):
                if guess_number[n] == key_game[n]:
                    cows += 1
                elif guess_number[n] in key_game:
                    bulls += 1
        print(cows, 'cows,', bulls, 'bulls.')
    return count

# file path: C:\Users\z003ar2v\PythonBeginner\pick-your-favorite\files_store_results.txt

with open('files_store_results.txt', 'a') as file:
    file.write(str(play(4)))
    file.write("\n")

infile = open('files_store_results.txt', 'r')
content = [float(line) for line in infile.readlines()]
infile.close()
min_value = min(content)
print("The best player's guessed the number in ", min_value, "attempt")
