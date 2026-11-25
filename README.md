# Password Checker and Generator

Lightweight Python code made to check passwords the user inputs and give a response. Also generates a password if the user chooses to do so. 


## Features

* **Password Check:** Allows users to input a password and be tested against certain rules. Depending on the score a certain message will appear. 
* **Password Generator:** Users can choose to have a password be generated using certain rules.


## Tech Used

* **Python3**
* Built-in libraries: `secrets`, `string`


## How to Use

1. Make sure Python3 is installed on your pc
2. Open password_tool in your terminal
3. Choose between `generate` or `check` when asked for an input
4. If `check` is entered the program will ask for a password and will be scored based on certain criteria (length, special characters, numbers, etc)
5. If `generate` is entered the program will create a new 12-character password.