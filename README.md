# Socket Programming
This is a simple calculator server that performs basic arithmetic operations on two numbers. It listens on a given port and waits for clients to connect. Upon receiving a connection request, it prompts the client for input and sends back the result.

## Prerequisites
Python 3.x
termcolor library

## How to Run
Run the servers by executing the ```python3 server_1.py``` OR ```python3 server_2.py``` file.
Connect to the server using the host ip and port.
Port Number for server_1.py is 11003
Port Number for server_2.py is 11004

## How to use
Enter an arithmetic expression with two operands and an operator, separated by spaces.
The server will send back the result of the calculation.

Usage Example: 1 + 1 + 1

## Files
server_1.py and server_2.py: The main server file that listens for incoming connections and performs the calculations.
README.md: The documentation file.

## How it Works
The server waits for incoming connections and accepts them.
Upon connection, it sends a greeting message and waits for user input.
If the user input is invalid or the user types "exit", the server closes the connection and waits for the next connection.

## Contributors
Prakhar Gupta (B21AI027)
Adarsh Shrivastav (B21AI003)