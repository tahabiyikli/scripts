import subprocess

input_file_path = 'domain.txt'
output_file_path = 'check.txt'

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    domains = input_file.read().splitlines()

    for domain in domains:
        try:
            # host komutu ile domainin alias bilgisini al
            result = subprocess.run(['host', domain], capture_output=True, text=True)
            output = result.stdout

            # Eğer alias bilgisi varsa, check.txt dosyasına yaz
            if 'alias' in output.lower():
                result_line = f"{domain} -> {output.strip()}"
                print(result_line)
                output_file.write(result_line + '\n')
            else:
                print(f"{domain} için alias bilgisi bulunamadı.")

        except subprocess.CalledProcessError as e:
            # host komutu hata verirse
            print(f"{domain} için host komutu çalıştırılırken hata oluştu: {e}")
