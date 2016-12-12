Разворачивание проекта на локалке
----------------------------------------

* sudo -u postgres createdb bulletin_board
* mkvirtualproject -p /usr/bin/python3 bulletin_board
* pip install -r requirements/development.txt
* ./manage.py migrate
* ./manage.py createsuperuser
* ./manage.py loaddata apps/boards/fixtures/fill_boards.json
* ./manage.py runserver
