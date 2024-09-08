"""
Vokabelbuch (Vocabulist) - Vocabulary List
"""

import os
import csv

# Vocabulary dictionary to store sords and their meanings
vocabulary = {}

# Function to display the main menu
def display_menu():
    print("\nVocabulary List")
    print("1. Add a new word")
    print("2. View all words")
    print("3. Search a word")
    print("4. Delete a word")
    print("5. Update a word")
    print("6. Save to file")
    print("7. Load from file")
    print("8. Exit")
    print()

# Function to add a new word to the vocabulary
def add_word():
    word = input("Enter the word: ").strip().lower()
    meaning = input("Enter the meaning: ").strip()
    if word in vocabulary:
        print(f"The word '{word}' already exists in your vocabulary.")
    else:
        vocabulary[word] = meaning
        print(f"The word '{word}' has been added.")

# Function to view all words in the vocabulary
def view_words():
    if not vocabulary:
        print("Your vocabulary is empty.")
    else:
        print("\nYour vocabulary list:")
        for word, meaning in vocabulary.items():
            print(f"{word}: {meaning}")

# Function to search for a word in the vocabulary
def search_word():
    word = input("Enter the word to search: ").strip().lower()
    meaning = vocabulary.get(word)
    if meaning:
        print(f"{word}: {meaning}")
    else:
        print(f"The word '{word}' was not found in your vocabulary.")

# Function to delete a word from the vocabulary
def delete_word():
    word = input("Enter the word to delete: ").strip().lower()
    if word in vocabulary:
        del vocabulary[word]
        print(f"The word '{word}' has been deleted.")
    else:
        print(f"The word '{word}' was not found in your vocabulary.")

# Function to update a word in the vocabulary
def update_word():
    word = input("Enter the word to update: ").strip().lower()
    if word in vocabulary:
        meaning = input("Enter the new meaning: ").strip()
        vocabulary[word] = meaning
        print(f"The word '{word}' has been updated.")
    else:
        print(f"The word '{word}' was not found in your vocabulary.")

# Function to save the vocabulary to a file
# def save_to_file():
#     filename = input("Enter the filename to save to: ").strip()
#     with open(filename, "w") as file:
#         for word, meaning in vocabulary.items():
#             file.write(f"{word}:{meaning}\n")
#     print(f"Your vocabulary has been saved to '{filename}'.")

# Function to save vocabulary to a CSV file
def save_to_csv():
    filename = input("Enter the filename to save to (with .csv extension): ").strip()
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Word", "Meaning"])
        for word, meaning in vocabulary.items():
            writer.writerow([word, meaning])
    print(f"Your vocabulary has been saved to '{filename}' as a CSV file.")

# Function to load the vocabulary from a file
# def load_from_file():
#     filename = input("Enter the filename to load from: ").strip()
#     if os.path.exists(filename):
#         with open(filename, "r") as file:
#             for line in file:
#                 word, meaning = line.strip().split(":")
#                 vocabulary[word] = meaning
#         print(f"Your vocabulary has been loaded from '{filename}'.")
#     else:
#         print(f"The file '{filename}' does not exist.")

# Function to load vocabulary from a CSV file
def load_from_csv():
    filename = input("Enter the filename to load from (with .csv extension): ").strip()
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                # if len(row) == 2:
                word, meaning = row
                vocabulary[word] = meaning
        print(f"Your vocabulary has been loaded from '{filename}' as a CSV file.")
    else:
        print(f"The file '{filename}' does not exist.")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your option: ").strip()

    if choice == "1":
        add_word()
    elif choice == "2":
        view_words()
    elif choice == "3":
        search_word()
    elif choice == "4":
        delete_word()
    elif choice == "5":
        update_word()
    elif choice == "6":
        # save_to_file()
        save_to_csv()
    elif choice == "7":
        # load_from_file()
        load_from_csv()
    elif choice == "8":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
