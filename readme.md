To run application
```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser # only one time
python manage.py runserver
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
. ./venv/bin/activate
# or source ./venv/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```