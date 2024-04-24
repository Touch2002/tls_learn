# tls_learn
спочатку потрібно додати readme файл до репозиторію
щоб переконатися що все працює, по скріну нижче 
показано команди які потрібно виконати.

![alt](img/firstgit.png "get certificate")
тобто я тупо скопіював команду і вбив в термінал
````
echo "# tls_learn" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Touch2002/tls_learn.git
git push -u origin main
````
Після виконання команди отримав такий вивід
![alt](img/error1.png "error")
За [посиланням](https://docs.github.com/en/authentication/troubleshooting-ssh/error-permission-denied-publickey),
першою командою я перевіряю чи був закритий ssh ключ згенерований раніше.
````
ssh-add -l -E sha256
````
![alt](img/ssh_key.png "private key")
Тепер переконуюсь що ssh приєднано до облікового запису

Запускаю агент ssh в фоновому режимі
````
eval "$(ssh-agent -s)"
````
Маю такий вивід
![alt](img/fonssh.png "ssh")
Знаходжу відбиток приватного ключа
````
ssh-add -l -E md5
````
Або
````
ssh-add -l
````
Отримав такий вивід
![alt](img/2error.png)

Так як результат не є очікуваним це можна вважати помилкою. Покищо це пропущу
і перейду за посиланням в якому пояснюється як ["Додати свій ключ SSH до github"](https://docs.github.com/en/authentication/troubleshooting-ssh/error-permission-denied-publickey),
після перечитання я просто поіншому гугланув і знайшов [статтю](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account),
там є команда
````
cat ~/.ssh/id_ed25519.pub
````
![alt](img/command.png)
закинув відкритий ключ в свій профіль
![alt](img/addsshkey.png)
Тепер начебто повинно працювати роблю пуш отримав такий вивід
![alt]