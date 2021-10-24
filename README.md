# ligmacy-pharma

Project for CSIT327 - F1. Made by [Kate Aubrey Cellan](https://github.com/DaijobuDes) and [Seejee Genegabuas](https://github.com/densentsu124).

Created using python django.

### Running
Clone this repository and `cd` into the cloned repository and inside `ligmacypharma`. 

After executing `cd`'s run `py manage.py makemigrations`, `py manage.py migrate` and finally `py manage.py runserver` to run the server.

### Disclaimer
This should not be deployed into the internet as this contain vulnerabilities and we have no plan to fix them. We are not responsible to any damage that the software has caused to the system.

### License
Project is licensed under GNU General Public License v3.0.

Please read the [LICENSE](https://github.com/DaijobuDes/ligmacy-pharma/blob/main/LICENSE) file for more details.

### Current Directory Structure
```
ligmacy-pharma
|   .gitignore
|   LICENSE
|   README.md
|
\---ligmacypharma
    |   db.sqlite3
    |   ligmacy-pharma.bsdesign
    |   manage.py
    |
    +---ligmacypharma
    |   |   asgi.py
    |   |   settings.py
    |   |   urls.py
    |   |   wsgi.py
    |   |   __init__.py
    |
    \---ligmacyweb
        |   admin.py
        |   apps.py
        |   forms.py
        |   models.py
        |   tests.py
        |   urls.py
        |   views.py
        |   __init__.py
        |
        +---migrations
        |   |   0001_initial.py
        |   |   0002_medicine.py
        |   |   0003_cart.py
        |   |   __init__.py
        |   |
        |   \---__pycache__
        |           [See .gitignore]
        |
        +---static
        |   \---assets
        |       +---bootstrap
        |       |   +---css
        |       |   |       bootstrap.min.css
        |       |   |
        |       |   \---js
        |       |           bootstrap.min.js
        |       |
        |       +---css
        |       |       Contact-Form-Clean.css
        |       |       Login-Form-Clean.css
        |       |       Login-Form-Dark.css
        |       |       Registration-Form-with-Photo.css
        |       |
        |       +---fonts
        |       |       ionicons.eot
        |       |       ionicons.min.css
        |       |       ionicons.svg
        |       |       ionicons.ttf
        |       |       ionicons.woff
        |       |
        |       +---img
        |       |       about.jpg
        |       |       background.jpg
        |       |       bg.jpg
        |       |       index-intro.jpg
        |       |       intro.jpg
        |       |       meeting.jpg
        |       |       products-01.jpg
        |       |       products-02.jpg
        |       |       products-03.jpg
        |       |       sign-up.png
        |       |       star-sky.jpg
        |       |
        |       \---js
        |               current-day.js
        |
        +---templates
        |       about.html
        |       add_medicine.html
        |       add_record.html
        |       cart.html
        |       contact.html
        |       dashboard.html
        |       index.html
        |       sign_in.html
        |       sign_up.html
        |
        \---__pycache__
                [See .gitignore]
```
