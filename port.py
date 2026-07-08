print("""
==============================
   PORT  NUMBER DETAILS
==============================
""")

port = int(input("Enter Port Number : "))

if port == 80:
    print("Service : Web", "Description : HTTP (unencrypted web traffic)")
elif port == 443:
    print("Service : Web", "Description : HTTPS (encrypted web traffic)")
elif port == 8080:
    print("Service : Web", "Description : HTTP alternate (proxies/dev servers)")

elif port == 25:
    print("Service : Email", "Description : SMTP (sending mail)")
elif port == 110:
    print("Service : Email", "Description : POP3 (retrieving mail)")
elif port == 143:
    print("Service : Email", "Description : IMAP (retrieving mail, syncs across devices)")
elif port == 465 or port == 587:
    print("Service : Email", "Description : SMTP over SSL/TLS")
elif port == 993:
    print("Service : Email", "Description : IMAPS")
elif port == 995:
    print("Service : Email", "Description : POP3S")

elif port == 20 or port == 21:
    print("Service : File Transfer", "Description : FTP (data/control)")
elif port == 22:
    print("Service : Remote Access / File Transfer", "Description : SSH / SFTP (secure remote access & file transfer)")
elif port == 69:
    print("Service : File Transfer", "Description : TFTP")

elif port == 23:
    print("Service : Remote Access", "Description : Telnet (unencrypted, largely deprecated)")
elif port == 3389:
    print("Service : Remote Access", "Description : RDP (Windows Remote Desktop)")
elif port == 5900:
    print("Service : Remote Access", "Description : VNC")

elif port == 53:
    print("Service : Naming", "Description : DNS")

elif port == 67 or port == 68:
    print("Service : Network Services", "Description : DHCP")
elif port == 123:
    print("Service : Network Services", "Description : NTP (time sync)")
elif port == 161 or port == 162:
    print("Service : Network Services", "Description : SNMP (network monitoring)")

elif port == 1433:
    print("Service : Database", "Description : Microsoft SQL Server")
elif port == 1521:
    print("Service : Database", "Description : Oracle DB")
elif port == 3306:
    print("Service : Database", "Description : MySQL / MariaDB")
elif port == 5432:
    print("Service : Database", "Description : PostgreSQL")
elif port == 6379:
    print("Service : Database", "Description : Redis")
elif port == 27017:
    print("Service : Database", "Description : MongoDB")

elif port == 445:
    print("Service : File Sharing", "Description : SMB (Windows file sharing)")

else:
    print("Your port number is not registered here")
