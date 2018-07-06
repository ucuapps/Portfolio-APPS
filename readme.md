# Portfolio APPS.UCU
Platform for APPS.UCU students

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
### Prerequisites :
```
sudo apt-get install python3-pip
sudo pip3 install virtualenv
```

### For development: 
```
virtualenv venv -p /usr/bin/python3.5
source venv/bin/activate

pip install -r requirements.txt
mkdir -p static/media static/static static/static-only

./manage.py makemigrations
./manage.py migrate
./manage.py collectstatic

# example of .env : .env-example
source .env

./manage.py runserver
```
## License
This project is licensed under the MIT License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ucuapps/Portfolio-APPS/blob/master/LICENSE)

## Versioning
1.0.0

## Authors

* [Kostyantyn Liepieshov](https://github.com/Inkognita)
* [Iryna Kostyshyn](https://github.com/irynakostyshyn)
* [Victoria Yuzkiv](https://github.com/victoria-yuzkiv)
* [Marta Lozynska](https://github.com/martalozynska)
* [Oles Kozak](https://github.com/famdrum)




