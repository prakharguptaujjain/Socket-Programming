# Server 1:

The script begins by importing necessary modules - os, subprocess, signal, sys, termcolor, and socket.

It then defines a function called "install_termcolor" that checks if the termcolor library is installed and installs it if it is not. This function is called at the beginning of the script to ensure that the termcolor library is available for use.

Next, a class called "calculator" is defined that encapsulates the functionality of the calculator. The class has several methods, including "init", "help", "invalid_input", "calculation", and "user_input".

The *init* method initializes some instance variables that will be used throughout the class, including a greeting message and a flag for indicating whether the user has chosen to exit the calculator.

The *help* method displays a help message to the user explaining how to use the calculator and what each operator does. The "invalid_input" method handles cases where the user inputs an invalid expression or inputs the word "exit" or "help". It returns an appropriate message to the user.

The *calculation* method performs the actual arithmetic calculation based on the operator and operands provided. It checks for division by zero and returns an error message if necessary.

The *user_input* method is the main method that takes a string input from the user, validates it, and returns the result of the calculation. It first counts the number of operators in the input expression and validates that there is exactly one operator. If there are multiple operators, it uses Python's eval() function to evaluate the expression. If there is only one operator, it splits the input expression into operands and passes them to the "calculation" method to perform the arithmetic calculation.

Finally, the script creates a socket object that listens on a specified port and waits for incoming connections from clients. Once a connection is established, the script accepts an input expression from the client, passes it to the "user_input" method for validation and calculation, and sends the result back to the client. This process continues until the server is closed forcefully.

# Server 2:

