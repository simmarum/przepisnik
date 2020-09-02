To run application
```
python -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser # only one time
./manage.py runserver
```

To run heroku
```
git push heroku master
```

To recreate heroku app
```
git commit --amend -C HEAD
git push heroku:master -f
```
To run dockerfile
```
docker build -t "webdev:Dockerfile" .
docker run -p 8000:8000 webdev:Dockerfile
```
To develop
```
python -m venv venv
. ./venv/bin/activate
# or source ./venv/bin/activate
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
```
Configure heroku
- https://devcenter.heroku.com/articles/heroku-cli
- https://github.com/heroku/heroku-repo#reset
- https://help.heroku.com/O0EXQZTA/how-do-i-switch-branches-from-master-to-main
Create translation
```
./manage.py makemessages -l pl -i "venv*" -d djangojs
find ./ -name django.po | grep -v venv
find ./ -name djangojs.po | grep -v venv
# add translation in "locale/pl/LC_MESSAGES/django.po" file
# add translation in "locale/pl/LC_MESSAGES/djangojs.po" file
./manage.py compilemessages -i "venv*"
```