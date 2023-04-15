# Socket Programming
This is a simple calculator server that performs basic arithmetic operations. It listens on a given port and waits for clients to connect. Upon receiving a connection request, it prompts the client for input and sends back the result.

## Prerequisites
Python 3.x \
termcolor library (this will automatically be installed if not already present)

## How to Run
Run the servers by executing the ```python3 server1.py``` OR ```python3 server2.py``` file. \
Connect to the server using the host ip and port. \
server1.py supports single client at a time \
server2.py supports multiple clients at a time \
Port Number for server is 

## How to use
Enter an arithmetic expression which you need to evaluate.
The server will send back the result of the calculation.

Usage Example: 1 + 1 + 1

## Files
server1.py and server2.py: The main server file that listens for incoming connections and performs the calculations. \
README.md: The documentation file. \
Check Detailed working at [SERVER_README.md](SERVER_README.md)

## How it Works
The server waits for incoming connections and accepts them.
Upon connection, it sends a greeting message and waits for user input.
If the user input is invalid or the user types "exit", the server closes the connection and waits for the next connection.

## Contributors
Prakhar Gupta (B21AI027) \
Adarsh Shrivastav (B21AI003)