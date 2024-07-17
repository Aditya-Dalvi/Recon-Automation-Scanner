import subprocess

def nmap_scan():
    target = input("Enter target: ")
    print("Select scan type:")
    print("1. SYN Scan (-sS)")
    print("2. Version Detection (-sV)")
    print("3. OS Detection (-O)")
    print("4. All Scans (-A)")
    scan_choice = input("Enter your choice: ")
    
    scan_type = {
        "1": "-sS",
        "2": "-sV",
        "3": "-O",
        "4": "-A"
    }.get(scan_choice, "-sS")
    
    print("Select scan Time and Performance:")
    print("1. wait 15 seconds and 0.4 seconds (-T1)")
    print("2. Faster than T1 (-T2)")
    print("3. Nmap's default behavior (-T3)")
    print("4. maximum TCP and SCTP scan delay to 10ms (-T4)")
    print("4. maximum TCP and SCTP scan delay to 5ms (-T5)")
    scan_choice = input("Enter your choice: ")

    speed_type = {
        "1": "-T1",
        "2": "-T2",
        "3": "-T3",
        "4": "-T4",
        "5": "-T5"
    }.get(scan_choice, "-T1")

    
    subprocess.run(["sudo", "nmap", scan_type, speed_type, target])

def nikto_scan():
    target_url = input("Enter target URL: ")
    options = input("Enter additional options (or press Enter for none): ").split()
    subprocess.run(["nikto", "-h", target_url] + options)

def sqlmap_scan():
    target_url = input("Enter target URL: ")
    print("Select technique:")
    print("1. Basic SQL Injection")
    print("2. Crawl and Scan")
    print("3. DBMS-specific (MySQL)")
    sqlmap_choice = input("Enter your choice: ")
    
    technique = {
        "1": "",
        "2": "--crawl=1",
        "3": "--dbms=mysql"
    }.get(sqlmap_choice, "")
    
    subprocess.run(["sqlmap", "-u", target_url] + technique.split())

def dnsrecon_scan():
    domain = input("Enter domain: ")
    print("Select scan type:")
    print("1. Standard Enumeration")
    print("2. Zone Transfer (-t axfr)")
    print("3. Brute Force (-D [wordlist] -t brt)")
    dnsrecon_choice = input("Enter your choice: ")
    
    if dnsrecon_choice == "3":
        wordlist_path = input("Enter path to wordlist: ")
        scan_type = f"-D {wordlist_path} -t brt"
    else:
        scan_type = {
            "1": "",
            "2": "-t axfr"
        }.get(dnsrecon_choice, "")
    
    subprocess.run(["dnsrecon", "-d", domain] + scan_type.split())

def dnsenum_scan():
    domain = input("Enter domain: ")
    print("Select scan type:")
    print("1. Standard Enumeration")
    print("2. Extended Enumeration (--enum)")
    dnsenum_choice = input("Enter your choice: ")
    
    options = {
        "1": "",
        "2": "--enum"
    }.get(dnsenum_choice, "")
    
    subprocess.run(["dnsenum", domain] + options.split())

def dirsearch_scan():
    url = input("Enter URL: ")
    wordlist_path = input("Enter path to wordlist: ")
    print("Select additional options:")
    print("1. Default")
    print("2. Recursive (-r)")
    print("3. Threads (-t)")
    dirsearch_choice = input("Enter your choice: ")
    
    if dirsearch_choice == "3":
        threads = input("Enter number of threads: ")
        options = f"-t {threads}"
    else:
        options = {
            "1": "",
            "2": "-r"
        }.get(dirsearch_choice, "")
    
    subprocess.run(["dirsearch", "-u", url, "-w", wordlist_path] + options.split())

def main():
    while True:
    
        print("  ____  __ __  ______   ___     _____   __   ____  ____   ____     ___  ____     ")
        print(" /    ||  |  ||      | /   \   / ___/  /  ] /    ||    \ |    \   /  _]|    \    ")
        print("|  o  ||  |  ||      ||     | (   \_  /  / |  o  ||  _  ||  _  | /  [_ |  D  )    ")
        print("|     ||  |  ||_|  |_||  O  |  \__  |/  /  |     ||  |  ||  |  ||    _]|    /     ")
        print("|  _  ||  :  |  |  |  |     |  /  \ /   \_ |  _  ||  |  ||  |  ||   [_ |    \     ")
        print("|  |  ||     |  |  |  |     |  \    \     ||  |  ||  |  ||  |  ||     ||  .  \    ")
        print("|__|__| \__,_|  |__|   \___/    \___|\____||__|__||__|__||__|__||_____||__|\_|    ")
        print("                                                                                  ")
        print("                                                                 ~ Aditya Dalvi   ")
        

        print("Select a tool to run:")
        print("1. Nmap")
        print("2. Nikto")
        print("3. SQLMap")
        print("4. dnsrecon")
        print("5. dnsenum")
        print("6. Dirsearch")
        print("7. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            nmap_scan()
        elif choice == "2":
            nikto_scan()
        elif choice == "3":
            sqlmap_scan()
        elif choice == "4":
            dnsrecon_scan()
        elif choice == "5":
            dnsenum_scan()
        elif choice == "6":
            dirsearch_scan()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please select a number from 1 to 7.")

if __name__ == "__main__":
    main()
