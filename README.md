# controlwork_9_abylay_kuvatov

## Superuser:
login: root
password: root

## Users:
1. johndoe
2. jackdoe
3. janedoe

password: 123456qWe!

## Для работы с проектом необходимо выполнить следующие действия:
1. склонировать проект в локальную папку
2. запустить приложение PyCharm и открыть папку проекта
3. PyCharm предложит установить виртуальное окружение и установить модули из файла requirements.txt
4. Нажмите Ок
5. Далее необходимо создать БД на локальном компьютере
6. В проекте, в приложении app открыть файл settings.py и добавить подключение к локальной БД:
`DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_user_password',
        'HOST': 'hostname',
        'PORT': '',
    }
}`
7. В терминале запустить команду python manage.py migrate, которая создаст в БД необходимые таблицы
8. Загрузить фикстуры командой -> python manage.py loaddata fixtures/dump.json
9. Запустить проект командой python manage.py runserver


## API:

Для проверки API можно воспользоваться программой **Postman**
##### Примечание: 
_Для проверки метода PUT, необходимо сначала получить данные определенной публикации, скопировать данные в окно BODY -> raw (JSON), затем внести изменения в необходимые поля и нажать на кнопку **Send**_

Также следует учесть, что права доступа разграничены согласно ТЗ, поэтому необходимо добавить в HEADERS следующие параметры: 
Key: Authorization
Value: Token _token_, где вместо _token_ необходимо вставить токен пользователя

#### tokens:

Чтобы сгенерировать токены, нужно сделать следующее:
В **Postman**, в окно BODY -> raw (JSON) добавить логин/пароль для пользователя в формате JSON:
{
    "username": _username_,
    "password": _password_
}
URL: POST http://localhost:8000/api/login/
