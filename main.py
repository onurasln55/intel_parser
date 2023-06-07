import os
import re

def remove_brackets(text):
    text = text.replace("[", "").replace("]", "")
    return text

def find_urls(text):
    urls = re.findall(r'\b(?:http|hxxp)s?://\S+\b', text, re.IGNORECASE)
    urls = list(set(urls))  # Yinelenen URL'leri kaldır
    urls = [url for url in urls if 'virustotal' not in url.lower()]
    return urls

def find_email_addresses(text):
    email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
    email_addresses = list(set(email_addresses))  # Yinelenen e-posta adreslerini kaldır
    return email_addresses

def find_ip_addresses(text):
    ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
    ip_addresses = list(set(ip_addresses))  # Yinelenen IP adreslerini kaldır
    return ip_addresses

def find_hashes(text):
    md5_hashes = re.findall(r'\b[A-Fa-f0-9]{32}\b', text)
    sha256_hashes = re.findall(r'\b[A-Fa-f0-9]{64}\b', text)
    hashes = list(set(md5_hashes + sha256_hashes))  # Yinelenen hash değerlerini kaldır
    return hashes

def process_text_file(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

            # [ ve ] karakterlerini kaldır
            text = remove_brackets(text)

            # URL'leri bul
            urls = find_urls(text)
            url_output_file = os.path.join('output', 'url.txt')
            with open(url_output_file, 'w') as url_file:
                url_file.write('\n'.join(urls))

            # E-posta adreslerini bul
            email_addresses = find_email_addresses(text)
            email_output_file = os.path.join('output', 'eposta.txt')
            with open(email_output_file, 'w') as email_file:
                email_file.write('\n'.join(email_addresses))

            # IP adreslerini bul
            ip_addresses = find_ip_addresses(text)
            ip_output_file = os.path.join('output', 'ip.txt')
            with open(ip_output_file, 'w') as ip_file:
                ip_file.write('\n'.join(ip_addresses))

            # Hash değerlerini bul
            hashes = find_hashes(text)
            hash_output_file = os.path.join('output', 'hash.txt')
            with open(hash_output_file, 'w') as hash_file:
                hash_file.write('\n'.join(hashes))

            print("İşlem tamamlandı. Çıktı dosyaları 'output' klasörüne kaydedildi.")
    except FileNotFoundError:
        print("Dosya bulunamadı.")


# Örnek kullanım
input_file = 'test.txt'  # İşlem yapılacak input dosyasının adı

# 'output' klasörünü oluştur
os.makedirs('output', exist_ok=True)

process_text_file(input_file)
