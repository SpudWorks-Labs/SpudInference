"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            Company: SpudWorks.
                        Program Name: SpudInference.
      Description: A low-end CPU friendly Local LLM Inference module.
                             File: main.py
                            Date: 2026/03/16
                        Version: 0.1.0-2026.03.16

===============================================================================

                        Copyright (C) 2026 SpudWorks Labs.

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU Affero General Public License as published
        by the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU Affero General Public License for more details.

        You should have received a copy of the GNU Affero General Public License
        along with this program. If not, see <https://www.gnu.org/licenses/>

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


import os
import sys

from engine.brain import chat


def print_menu():
    commands = {
        '/chat': "Chat to The SpudBrain.",
        '/convert': "Convert datasets for training.",
        '/exit': "Quit the program.",
        '/help': "Display more commands that are available.",
        '/train': "Start the training tool"
    }

    print("Welcome to SpudInference!\n\nHere are the available commands:\n")

    for cmd, desc in commands.items():
        print(f"\t{cmd} : {desc}")


def clear():
    os.system('clear' if sys.platform != 'nt' else 'cls')


def wait():
    input("\n\nPress enter to continue...")


def help_menu():
    clear()

    commands = {
        '/chat': "Chat to The SpudBrain.",
        '/convert': "Convert datasets for training.",
        '/exit': "Quit the program.",
        '/help': "Display all of the available commands.",
        '/train': "Start training a model with a dataset.",
        '/clear': "Clear the entire terminal screen."
    }


    print("Here are all of the available commands:\n")

    for cmd, desc in commands.items():
        print(f"\t{cmd}: {desc}")

    wait()


def main():
    clear()

    while True:
        print_menu()

        user_input = input("\n\n>>> ").lower()

        if user_input == '/exit':
            break
        elif user_input == '/train':
            # train.py / clean_tensors.py
            print("Training hook in progress!")

            wait()
        elif user_input == '/convert':
            # dataset_handling.py
            print("Conversion hook in progress!")
        elif user_input == '/chat':
            clear()
            chat()

        elif user_input == '/clear':
            clear()
            continue

        elif '/help':
            help_menu()

        else:
            print(f"Sorry, '{user_input}' is not a valid command!")

            wait()

        clear()


if __name__ == '__main__':
    main()

    print("Good-bye, thank you for using SpudInference!")
