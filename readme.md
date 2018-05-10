# Portfolio APPS.UCU

_Pre-requirements_:
```
sudo apt-get install python3-pip
sudo pip3 install virtualenv
```

_For development:_
```
virtualenv venv -p /usr/bin/python3.5
source venv/bin/activate

pip install -r requirements.txt
mkdir -p static/media static/static static/static-only

./manage.py makemigrations
./manage.py migrate
./manage.py collectstatic
./manage.py runserver
```

### _Good luck_
