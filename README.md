# Hello Wordle – Pokémon Edition

![Image](https://github.com/user-attachments/assets/d89d61a5-132e-41a1-8f13-3fef25b11bcb)

## Summary
Hello Wordle is a Python-based Wordle-style game with a twist – it's built using themed word lists like Pokémon names! This project focuses on creating a modular, reusable, and beginner-friendly word game that allows users to guess hidden words. The project demonstrates clean class design, file handling, user interaction, and logic implementation in Python.

## Introduction
The Hello Wordle project is designed as a playful way to apply foundational Python programming skills. It includes:
- Reading and cleaning word lists from a file  
- Random word selection as the secret answer  
- Validating user guesses  
- Tracking guess history and providing feedback  
- Displaying progress after each guess  

All logic is encapsulated within Python classes and follows Pythonic principles and best practices, making the code easy to read and extend.

## Gameplay Features
The program allows users to:
- **Play a Wordle-style guessing game** using Pokémon names or other word themes  
- **See feedback** on each guess to improve accuracy  
- **Continue guessing until the correct word is found**  
- **Interact via the terminal** with clear and clean prompts  

### Core Mechanics
- A random word is selected from a pre-cleaned list.  
- The player continues guessing until they find the correct word.  
- After each guess, feedback is given on which letters are correct and in the right position.

### File Handling
- Word data is stored in a text file (e.g., `week1_pokemon.txt`)  
- Words are cleaned, lowercased, and stripped of excess whitespace before gameplay begins.

### Planned Features
This project is built to be **easily extended** with additional word themes. While the current version uses a Pokémon-themed word list, upcoming updates may include:
- **Star Wars characters or ships**
- **League of Legends champions**
- **Other pop culture themes**

This modular design makes it simple to plug in new `.txt` files with different word banks for endless replayability and customisation.

## Tools
- Python 3.13  
- PyCharm, VSCode, or any other Python IDE  
- Git for version control  

## Files
- `hello_wordle.py` – The main game logic written as a class (`HelloWordle`).  
- `week1_pokemon.txt` – A word bank containing comma-separated Pokémon names.  
- `README.md` – Project documentation.  

## Usage
To play the game, run the `hello_wordle.py` file from the terminal or your preferred Python IDE:

```sh
python hello_wordle.py
