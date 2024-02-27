import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "IP adresi bulunamadı."

# Domain dosyasını oku
with open("domain.txt", "r") as domain_file:
    domains = domain_file.read().splitlines()

# IP adreslerini bul ve ip.txt dosyasına yaz
with open("ip.txt", "w") as ip_file:
    for domain in domains:
        ip_address = get_ip_address(domain)
        ip_file.write(f"{domain}: {ip_address}\n")

print("IP adresleri başarıyla ip.txt dosyasına yazıldı.")
