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
        Loads words from a given file, cleans and stores them
        :param file_path: theme specific
        :return: list of iterable words/name in lowercase
        """
        with open(file_path) as f:
            # Read the entire file into one long string
            contents = f.read()

        raw_names = (contents.split(","))

        # Loop through the list and clean each name and append to "clean_names" list
        self.clean_names = [name.lower().strip() for name in raw_names]

        print(f"\n{self.clean_names[:5]}")  # Print to test

        # KNOWLEDGE TEST : The lengths of all Pokémon names in self.clean_names, but only if the name starts with the letter “c”?
        self.test = [(name, len(name)) for name in self.clean_names if name[0] == "c"]
        print(f"\n{self.test}")


game = HelloWordle()



