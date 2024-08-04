import random as r

rand_num = r.randrange(1, 20)   # Generating a random number betwen 1 and 19
print(f'Number to be guessed : {rand_num}')

i = 1
while True:
    print(f"Number Guessed : {i}")
    if (i == rand_num):  # If the number guessed is correct this  blok will be executed
        print("Random number has been guessed succesfully!")
        break # Break statements stops and exits from loop

    i += 1 

print("End of program...")