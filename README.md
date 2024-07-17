# Recon-Automation-Scanner

This Python script is a command-line interface (CLI) tool that allows users to perform various security scans using popular tools such as Nmap, Nikto, SQLMap, dnsrecon, dnsenum, and Dirsearch.

Imports:

python
Copy code
import subprocess
The subprocess module is imported to allow the script to run system commands.

Nmap Scan Function:

def nmap_scan():
Prompts the user for a target IP or hostname.
Presents a menu to select the type of Nmap scan.
Presents another menu to select the timing and performance options for the scan.
Constructs the Nmap command and executes it using subprocess.run.

Nikto Scan Function:

def nikto_scan():
Prompts the user for a target URL.
Optionally allows additional Nikto options.
Constructs the Nikto command and executes it.

SQLMap Scan Function:

def sqlmap_scan():
Prompts the user for a target URL.
Presents a menu to select the SQL injection technique.
Constructs the SQLMap command and executes it.

dnsrecon Scan Function:

def dnsrecon_scan():
Prompts the user for a domain.
Presents a menu to select the type of DNS recon scan.
If brute force is selected, it prompts for a wordlist path.
Constructs the dnsrecon command and executes it.

dnsenum Scan Function:

def dnsenum_scan():
Prompts the user for a domain.
Presents a menu to select the type of DNS enumeration.
Constructs the dnsenum command and executes it.

Dirsearch Scan Function:

def dirsearch_scan():
Prompts the user for a URL and a wordlist path.
Presents a menu for additional options such as recursion or threading.
If threading is selected, it prompts for the number of threads.
Constructs the Dirsearch command and executes it.

Main Menu:

def main():
Displays an ASCII art banner and the author's name.
Presents a menu for the user to select which tool to run.
Calls the corresponding function based on the user’s choice.
Includes an option to exit the program.

Entry Point:

if __name__ == "__main__":
    main()
Ensures the main function is called when the script is executed directly.
Example Execution Flow
User runs the script.
The main menu is displayed.
User selects a tool (e.g., Nmap).
The script prompts for target details and scan options.
The selected scan is performed using the appropriate tool.
Output from the scan is displayed in the terminal.
The main menu is re-displayed for further selections or exit.
This script effectively automates the use of several common security tools, providing a simple CLI interface for performing various types of security scans.
