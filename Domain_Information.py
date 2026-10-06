import whois

domain = input("Enter the domain (e.g. google.com): ")
info = whois.whois(domain)

print(f"Register: {info.registrar}")
print(f"Created: {info.creation_date}")
print(f"Expires: {info.expiration_date}")



