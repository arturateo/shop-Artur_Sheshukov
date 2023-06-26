# Приложение магазина

## Этапы установки приложения:

* Этап №1
  * Создайте папку для проекта 
  * Клонируйте проект в папку с помощью командной строки
    *       git clone git@github.com:arturateo/shop-Artur_Sheshukov.git
* Этап №2
    * Установите виртуальное окружение 
      *     python -m venv venv 
    * Установите все нужные библиотеки
      *     pip install -r requirements.txt
* Этап №3
  * Переименуйте файл .env_example в .env
    * Измените файл .env на ваши данные
      *     SECRET_KEY=SECRET_KEY
      
            NAME=NAME
            USER=USER
            PASSWORD=PASSWORD
            HOST=HOST
            PORT=PORT
  * Выполнить миграции 
    *       python manage.py migrate
  * Выгрузить фикстуры в БД 
    *       python manage.py loaddata fixtures/dump.json

#### Теперь можно пользоваться приложением
```
Логин/пароль от админ панели: admin
```
