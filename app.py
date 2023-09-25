# Import necessary modules
from socket import *  # Import the socket module for network communication
import time  # Import the time module to measure execution time
import sys  # Import the sys module for program exit

# Define a function called portScan
def portScan():
    # Prompt the user to enter a target hostname or IPv4 address
    targetName = input('Enter the target hostname or IPv4 address for port scanning: ')

    # Prompt the user to enter the start and end port numbers for scanning
    startPortNumber = int(input('Enter the START port number to scan: '))
    endPortNumber = int(input('Enter the END port number to scan: '))
    
    # Check if endPortNumber is greater than startPortNumber
    if endPortNumber <= startPortNumber:
        print("Error: End port number must be larger than Start port number")
        sys.exit(1)  # Exit the program with an error code

    # Convert the target hostname to its corresponding IPv4 address
    targetIPv4 = gethostbyname(targetName)

    # Print the target IPv4 address
    print ('Starting scan on: ', targetIPv4)
    
    # Loop through the range of port numbers specified by the user
    for portNumber in range(startPortNumber, endPortNumber + 1): # Added 1 to Include endPortNumber in the loop. You can remove it to see the effect.
        # Create a socket object for IPv4 and TCP communication
        sockets = socket(AF_INET, SOCK_STREAM)
        
        # Print the host being scanned and the port number being checked
        print ('Scanning host: ', targetIPv4, ' on Port: ', portNumber)
        
        # Attempt to establish a connection with the target on the specified port
        connection = sockets.connect_ex((targetIPv4, portNumber))
        
        # Check if the connection was successful (port is open)
        if(connection == 0):
            print ('Port %d: OPEN' % (portNumber,))
        
        # Close the socket
        sockets.close()

# Record the start time of the program execution
programStartTime = time.time()

# Call the portScan function to start scanning ports
portScan()

# Calculate and print the time taken for the scan
print('Time taken:', time.time() - programStartTime)
