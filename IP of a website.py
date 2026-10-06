import socket

website = input("Enter the web address ")
ip = socket.gethostbyname(website)

print(f"IP of the {website} is {ip}")
