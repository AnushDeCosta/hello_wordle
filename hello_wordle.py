# Open file and automatically close it when done
import random

with open("week1_pokemon.txt") as f:
    # Read the entire file into one long string
    contents = f.read()

# Show all content
print(contents)

# Split the Pokemon names ad delimiter ","
all_pokemon = (contents.split(","))
print(all_pokemon[1].title().strip()) # Print output for testing

# Create new list to store Cleaned Pokemon names
clean_names = []

# Loop through the list and clean each name and append to "clean_names" list
for name in all_pokemon:
    name = name.upper().strip()
    clean_names.append(name)
    print(f"<{name}>") # Print to test

# Let Computer choose a random word
random.seed(115) #Seed the randomness for repetition
secret_word = random.choice(clean_names)
print(secret_word) #Print the word for testing