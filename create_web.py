from flask import Flask
from OpenSSL import crypto

app = Flask(__name__)


def generate_self_signed_cert(cert_file, key_file):
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    cert = crypto.X509()
    cert.get_subject().C = "US"  # Країна
    cert.get_subject().ST = "New York"  # Регіон/штат
    cert.get_subject().L = "New York"  # Місто
    cert.get_subject().O = "Example"  # Організація
    cert.get_subject().CN = "example.com"  # Загальне ім'я
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)  # Дійсний термін сертифіката (10 років)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, 'sha256')

    with open(cert_file, "wb") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    with open(key_file, "wb") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))


@app.route("/")
def hello():
    return "Hello, World! This is a secure webpage."


if __name__ == "__main__":
    generate_self_signed_cert("cert.pem", "key.pem")
    app.run(ssl_context=("cert.pem", "key.pem"), debug=True)
