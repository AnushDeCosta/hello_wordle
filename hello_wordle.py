# This is a Wordle-like game blueprint

class HelloWordle:
    """
    A Wordle-style game using different themes such as Pokemon names.
    Handles loading, cleaning, and selecting a secret word.
    """
    def __init__(self):
        pass

    def load_words(self, file_path):
        """
        Loads and cleans word data from a text file.
        :param file_path: The path to the text file containing a comma-separated list of words.
        :return: None – stores a cleaned list of lowercase words in self.clean_names.
        """
        with open(file_path) as f:
            # Read the entire file into one long string
            contents = f.read()

        raw_names = (contents.split(","))

        # Loop through the list and clean each name and append to "clean_names" list
        self.clean_names = [name.lower().strip() for name in raw_names]
        # KNOWLEDGE TEST : The lengths of all Pokémon names in self.clean_names, but only if the name starts with the letter “c”?
        # self.test = [(name, len(name)) for name in self.clean_names if name[0] == "c"]


    def choose_word(self):
        """
        Selects a random word from the loaded word list.
        :return: a hidden random "chosen" word in dashes instead of letters.
        """
        import random
        random.seed(115)  # Lock randomness for testing
        self.secret_word = random.choice(self.clean_names)
        print(f"Testing - {self.secret_word}")  # Print the word for testing

    def display_word(self, word, guessed_letters):
        """
        Displays the current progress of the guessed word.
        :param word: The full secret word that the player is trying to guess.
        :param guessed_letters: A list of letters that have been guessed so far.
        :return: None - prints the word with the guessed letters revealed and
                 others hidden as "_"
        """
        progress = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(progress))

    def play_game(self):
        """
        Runs the main game loop for HelloWordle.
        This method:
        - Initializes a list of guessed letters and turn counter.
        - Repeatedly displays word progress and asks for user input.
        - Validates input and prevents duplicate guesses.
        - Reveals letters based on correct guesses.
        - Ends the game when the full word is revealed.
        :return: None – prints progress and result to the console.
        """
        guessed_letters = []
        turns = 0
        while not all(letter in guessed_letters for letter in self.secret_word):
            print()
            print("*" * 30)
            print(f"Turn: {turns}\n")
            self.display_word(self.secret_word, guessed_letters)
            print(f"\nLetters guessed: {guessed_letters}")
            valid_guess = False
            while not valid_guess:
                guess = input("Guess a letter: ").lower().strip()
                if len(guess) != 1:
                    print("Too many characters")
                elif not guess.isalpha():
                    print("Invalid input. Please enter a letter from A-Z.")
                elif guess in guessed_letters:
                    print("You already guessed that letter")
                else:
                    valid_guess = True
                    guessed_letters.append(guess)
                    turns += 1
        else:
            # Game complete message
            print("\nCongratulations! You guessed the word correctly 🎉")
            print(f"The word was: '{(self.secret_word).upper()}'")
            print(f"It took you {turns} turns.")


game = HelloWordle()
game.load_words("week1_pokemon.txt")
game.choose_word()
game.play_game()

