```markdown
# Port Scanner

A simple Python script to scan for open ports on a target host.

## Usage

1. Clone this repository to your local machine.

2. Run the script by executing the following command in your terminal:

   ```bash
   python app.py
   ```

3. Follow the on-screen prompts to enter the target hostname or IPv4 address and the range of ports to scan.

4. The script will then scan the specified range of ports and display the results.

## How it Works

The script performs the following steps:

1. Imports necessary modules, including `socket` and `time`.

2. Defines a `portScan` function for the port scanning process.

   - It prompts the user for target information, validates the input, and resolves the target's IPv4 address.

   - It loops through a range of port numbers, attempts to establish a connection, and reports open ports.

3. Records the start time of the program and calls the `portScan` function.

4. Calculates and prints the time taken for the scanning process.

## Example

Here's an example of how to use the port scanner:

```bash
Enter the target hostname or IPv4 address for port scanning: example.com
Enter the START port number to scan: 80
Enter the END port number to scan: 85

Starting scan on: 93.184.216.34
Scanning host: 93.184.216.34 on Port: 80
Port 80: OPEN
Scanning host: 93.184.216.34 on Port: 81
Scanning host: 93.184.216.34 on Port: 82
Scanning host: 93.184.216.34 on Port: 83
Scanning host: 93.184.216.34 on Port: 84
Scanning host: 93.184.216.34 on Port: 85

Time taken: 0.36109209060668945 seconds
```

## License

This project is licensed under The Unlicense License.
```