from cryptography import x509
from cryptography.hazmat.backends import default_backend
import ssl


def hex_to_colums(number):
    ser_number = number
    ser_hex = str(hex(ser_number))[2:]
    if len(ser_hex[2:]) % 2 != 0:
        ser_hex = "0" + ser_hex
    hex_with_colons = ':'.join(ser_hex[i:i + 2] for i in range(0, len(ser_hex), 2))
    return hex_with_colons


def get_from_server(host, port):
    port = 443
    cert = ssl.get_server_certificate((host, port))
    return cert


def show_result(cert):
    certDecoded = x509.load_pem_x509_certificate(str.encode(cert), default_backend())

    num = certDecoded.serial_number
    hex_with_colons = hex_to_colums(num)

    open_key = certDecoded.public_key().public_numbers().n
    hex_key = hex_to_colums(open_key)

    n = [
        hostname,
        certDecoded.version,
        certDecoded.serial_number,
        f"serial hex {hex_with_colons}",
        certDecoded.signature_algorithm_oid._name,
        certDecoded.issuer,
        certDecoded.not_valid_before_utc,
        certDecoded.not_valid_after_utc,
        certDecoded.signature_algorithm_parameters.name,
        certDecoded.public_key().key_size,
        certDecoded.public_key().public_numbers(),
        f"open key as hex {hex_key}"


    ]

    return [print(i) for i in n]


def save_certificate(host, port):
    cert = ssl.get_server_certificate((host, port))
    with open("certificate.pem", "w", encoding="utf-8") as file:
        # Записуємо текст у файл
        file.write(cert)


def open_certificate(path):
    with open(path, 'r') as cert_content:
        cert_data = cert_content.read()
    return show_result(cert_data)


hostname = "desmos.com"
port = 443

#cert = get_from_server(hostname, port)
#print(show_result(cert))

#print(type(certDecoded.public_key()))

#save_certificate(hostname, port)

certfile = "_.desmos.com"
print(open_certificate(certfile))
