import os
import subprocess
import signal
import sys

#For installing termcolor library if client does not have termcolor library
def install_termcolor():
    # Check if termcolor is installed
    try:
        import termcolor
    except:
        # Check if pip3 is installed
        try:
            subprocess.check_call(['pip3', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.check_call(['pip3', 'install', 'termcolor'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            # Check if pip is installed
            try:
                subprocess.check_call(['pip', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.check_call(['pip', 'install', 'termcolor'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except:
                pass

# Call the install_termcolor function
install_termcolor()

import termcolor

# Define the calculator function
class calculator:
    #Initialisation
    def __init__(self):
        #greeting , example and exit
        self.returning_result = []
        self.greetings = termcolor.colored("\n [Welcome!! \n For help type 'help' \n To exit the calculator, type 'exit' \n Usage Example: 1 + 1 + 1]",'green')
        self.exit=False
    
    #Help function
    def help(self,returning_result):
        #Usage of the calculator
        returning_result.append(termcolor.colored("How to use?","yellow"))
        returning_result.append(termcolor.colored("Format:","yellow"))
        returning_result.append(termcolor.colored("operand operator operand ...","yellow"))
        #function of each operator
        returning_result.append(termcolor.colored("Function of each operator:","yellow"))
        returning_result.append(termcolor.colored("+: Addition","yellow"))
        returning_result.append(termcolor.colored("-: Subtraction","yellow"))
        returning_result.append(termcolor.colored("*: Multiplication","yellow"))
        returning_result.append(termcolor.colored("/: Division","yellow"))
        returning_result.append(termcolor.colored("%: Modulo","yellow"))
        returning_result.append(termcolor.colored("**: Exponentiation","yellow"))
        return returning_result
    
    #Invalid_input function
    def invalid_input(self, returning_result,user_input):
        if "exit" in user_input:
            returning_result.append(termcolor.colored("Exiting the calculator...", 'red'))
            self.exit=True
            return returning_result
        if "help" in user_input:
            returning_result=self.help(returning_result)
        else:
            #invalid input
            returning_result.append(termcolor.colored("Invalid input!", 'red'))
            returning_result.append("If you want further help, type 'help'")
            returning_result.append("To exit the calculator, type 'exit'")
        return returning_result
    
    #Main calcualtion part by calculator
    def calculation(self, operator_code, operand1, operand2):
        try:
            operand1 = float(operand1)
            operand2 = float(operand2)
        except:
            return self.invalid_input([],"invalid")

        # perform the calculation
        if operator_code == 1:
            result = float(operand1) + float(operand2)
        elif operator_code == 2:
            result = float(operand1) - float(operand2)
        elif operator_code == 3:
            result = float(operand1) * float(operand2)
        elif operator_code == 4:
            if(abs(float(operand2) - 0)<1e-6):
                return [termcolor.colored("Error: Division by zero is not possible!", 'red')]
            result = float(operand1) / float(operand2)
        elif operator_code == 5:
            result = float(operand1) % float(operand2)
        elif operator_code == 6:
            result = float(operand1) ** float(operand2)

        return [str(result)]
    
    #Takes user_input and validates the expression
    def user_input(self,given_input):
        # get input from the user
        returning_result = []

        operators=["+", "-", "*", "/", "%", "**"]
        # perform the calculation

        #Counting number of operators
        cnt = 0
        valid_operator = False
        for operator in operators:
            for char in given_input:
                if char == operator:
                    valid_operator = True
                    operator_code = operators.index(operator) + 1
                    cnt += 1

        
        if not valid_operator:
            returning_result=self.invalid_input(returning_result,given_input)
            return returning_result

        #If number of operator is greater than 1
        #Then by using eval function, evaluating the input
        if cnt > 1:
            try:
                return [str(eval(given_input))]
            except:
                return self.invalid_input([],"invalid")
        else:
            # split the user input into a list
            given_input = given_input.split(operators[operator_code-1])
            result=self.calculation(operator_code, given_input[0], given_input[-1])
            returning_result += result
        return returning_result

#Importing socket library
import socket

# Created Socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 11003

print(f"Server is running on port number {port}")
server_socket.bind((host, port))

#Run till server is not closed forcefully
while True:

    # Listen for incoming connections only 1
    server_socket.listen(1)
    client_socket, client_address = server_socket.accept()

    print('Connected to:', client_address)

    data = client_socket.recv(1024)
    calc = calculator()
    decoded_data=data.decode()

    print(f"Client({client_address}) -> server : {decoded_data}")
    
    returning_result=calc.user_input(data.decode())
    
    output = ""
    if (calc.exit):
        client_socket.close()
        continue
    for result in returning_result:
        output += result + "\n"

    if not data:
        client_socket.close()
        continue

    if "help" not in decoded_data:  
        output = output + "\n" + calc.greetings

    client_socket.send((output).encode())

    print(f"server -> client({client_address}) : {output}")

    #Run till client is connected
    while True:
        data = client_socket.recv(1024)

        print(f"Client({client_address}) -> server : {data.decode()}")
        returning_result=calc.user_input(data.decode())

        output = ""
        if (calc.exit):
            break
        for result in returning_result:
            output += result + "\n"

        if not data:
            break
        client_socket.send((output).encode())
        print(f"server -> client({client_address}) : {output}")

    # close the connection
    client_socket.close()
