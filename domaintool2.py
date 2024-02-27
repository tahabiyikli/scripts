import subprocess

# kapsam.txt dosyasını httprobe ile tarayarak url.txt dosyasına yazma
httprobe_command = "cat kapsam.txt | httprobe -c 50 -t 3000 > url.txt"
subprocess.run(httprobe_command, shell=True)

# url.txt dosyasındaki URL'leri çıkarma ve sort -u ile sıralayarak domain.txt dosyasına yazma
extract_domain_command = "grep -oP \"(?<=://)\\S+\" url.txt | sort -u > domain.txt"
subprocess.run(extract_domain_command, shell=True)

# kapsam.txt ve domain.txt dosyalarını oku
with open('kapsam.txt', 'r') as kapsam_file:
    kapsam_lines = set(kapsam_file.readlines())

with open('domain.txt', 'r') as domain_file:
    domain_lines = set(domain_file.readlines())

# kapsam.txt ve domain.txt dosyalarını karşılaştırarak unreach.txt dosyasına yazma
unreach_lines = kapsam_lines - domain_lines
with open('unreach.txt', 'w') as unreach_file:
    unreach_file.writelines(sorted(unreach_lines))

print("İşlem tamamlandı.")
