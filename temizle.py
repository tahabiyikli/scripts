import re

def extract_domains(text):
    # Domainleri bulmak için regex kullanıyoruz
    domain_pattern = re.compile(r'\b(?:https?://)?(?:www\.)?([a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+)\b')
    matches = domain_pattern.findall(text)
    return matches

def write_to_file(domains):
    with open('kapsam.txt', 'w') as file:
        for domain in domains:
            file.write(domain + '\n')

if __name__ == "__main__":
    # Metni içeren dosyanın adını belirt
    with open('metin.txt', 'r') as file:
        content = file.read()

    # Domainleri çıkar
    domains = extract_domains(content)

    # Domainleri dosyaya yaz
    write_to_file(domains)

    print("Domainler başarıyla 'kapsam.txt' dosyasına yazıldı.")
