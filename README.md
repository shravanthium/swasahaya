# Swasahaya(ಸ್ವಸಹಾಯ) 
 A self help portal


## Running Locally

Make sure you have Python 3.7 , as well as Postgres

```sh
$ cd swasahaya

$ python3 -m venv swasahaya
$ pip install -r requirements.txt

$ createdb swasahaya

$ python manage.py migrate
$ python manage.py collectstatic
