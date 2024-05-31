from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World! This is a secure webpage."


if __name__ == "__main__":
    print("Привіт, моя задача підняти веб-сторінку зі згенерованим сертифікатом в openssl, розмісти в каталозі зі "
          "мною сертифікат і зміни його назву на 'cert.pem', і приватний ключ як 'key.pem'")
    try:
        app.run(ssl_context=("cert.pem", "key.pem"), debug=True)
    except FileNotFoundError:
        print("Файли не знайдено, перейменуйте або додайте до каталогу та перезавантажте програму")
        input()
