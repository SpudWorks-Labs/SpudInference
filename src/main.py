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


from engine.brain import chat


def print_menu():
    print("Welcome to SpudInference!\n\nHere are the available commands:\n")
    print("\t/chat : Chat to the LLM.\n\t/train : Start the training tool")
    print("\t/convert : Convert datasets for training.\n\t/exit : Quit the program.")


def main():
    while True:
        print_menu()

        user_input = input(">>> ").lower()

        if user_input == '/exit':
            break
        elif user_input == '/train':
            # train.py / clean_tensors.py
            pass
        elif user_input == '/convert':
            # dataset_handling.py
            pass
        elif user_input == '/chat':
            chat()
        else:
            print("Sorry, that is not a valid command!")


if __name__ == '__main__':
    main()

