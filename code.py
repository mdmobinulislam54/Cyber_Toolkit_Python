banner = r"""
 _____   _____   _____   _   _   _____
|  __ \ |  __ \ |_   _| | \ | | / ____|
| |__) || |__) |  | |   |  \| || |
|  ___/ |  _  /   | |   | . ` || |
| |     | | \ \  _| |_  | |\  || |____
|_|     |_|  \_\|_____| |_| \_| \_____|
"""

print(banner)
def port_lookup(port):
    ports = {
    # Web Services
    80: "Service: Web | HTTP - Unencrypted web traffic",
    443: "Service: Web | HTTPS - Encrypted web traffic",
    8080: "Service: Web | HTTP Alternate - Development servers / Proxies",
    8443: "Service: Web | HTTPS Alternate",
    # Email Services
    25: "Service: Email | SMTP - Sending emails",
    110: "Service: Email | POP3 - Receiving emails",
    143: "Service: Email | IMAP - Email synchronization",
    465: "Service: Email | SMTPS - Secure SMTP",
    587: "Service: Email | SMTP Submission",
    993: "Service: Email | IMAPS - Secure IMAP",
    995: "Service: Email | POP3S - Secure POP3",
    # File Transfer
    20: "Service: File Transfer | FTP Data",
    21: "Service: File Transfer | FTP Control",
    22: "Service: Remote Access | SSH / SFTP",
    69: "Service: File Transfer | TFTP",
    # Remote Access
    23: "Service: Remote Access | Telnet",
    3389: "Service: Remote Access | RDP (Remote Desktop)",
    5900: "Service: Remote Access | VNC",
    # DNS & Network
    53: "Service: Network | DNS",
    67: "Service: Network | DHCP Server",
    68: "Service: Network | DHCP Client",
    123: "Service: Network | NTP (Time Sync)",
    161: "Service: Network | SNMP",
    162: "Service: Network | SNMP Trap",
    # Windows Services
    135: "Service: Windows | RPC",
    137: "Service: Windows | NetBIOS Name Service",
    138: "Service: Windows | NetBIOS Datagram",
    139: "Service: Windows | NetBIOS Session",
    445: "Service: Windows | SMB File Sharing",
    # Databases
    1433: "Service: Database | Microsoft SQL Server",
    1521: "Service: Database | Oracle Database",
    3306: "Service: Database | MySQL / MariaDB",
    5432: "Service: Database | PostgreSQL",
    6379: "Service: Database | Redis",
    27017: "Service: Database | MongoDB",
    # Directory Services
    389: "Service: Directory | LDAP",
    636: "Service: Directory | LDAPS",
    # Security
    1812: "Service: Authentication | RADIUS",
    1813: "Service: Accounting | RADIUS",
    # VPN
    500: "Service: VPN | ISAKMP / IKE",
    1701: "Service: VPN | L2TP",
    1723: "Service: VPN | PPTP",
    # Miscellaneous
    514: "Service: Logging | Syslog",
    2049: "Service: Network File System | NFS",
    5060: "Service: VoIP | SIP",
    5061: "Service: VoIP | SIP over TLS"
}
    print(ports.get((port),"Port not registered"))
def check_url(url):
    if url.startswith("https"):
        print("Secure Website")
    else:
        print("Not secure Website")
def check_file(filename):
    if filename.endswith(".exe"):
        print("Executable file")
    else:
        print("Safe file")
def pas_strength(pas):
    if len(pas) >= 8 :
        print("Password is strong.")
    else:
        print("Password is weak.")
while True:
    print("""
    ===== Cyber Tool ===== 
    1. Port Lookup
    2. Check URL
    3. Check File
    4. Password Strength
    5. Exit
    ..................by mObInUl
    """)
    choice = int(input("Choose an option:"))
    if choice == 1 : 
        port = int(input("Enter a port:"))
        port_lookup(port)
    elif choice == 2:
        url = input("Enter an url:")
        check_url(url)
    elif choice == 3 :
        filename = input("Enter a file name:")
        check_file(filename)
    elif choice == 4 :
        pas = input("Enter a password:")
        pas_strength(pas)
    elif choice == 5 :
        break 
    else:
        print("Invalid input.")
