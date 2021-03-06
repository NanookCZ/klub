Auto\*mat klub
============
[![Build Status](https://travis-ci.org/auto-mat/klub.svg?branch=master)](https://travis-ci.org/auto-mat/klub)
[![Coverage Status](https://coveralls.io/repos/github/auto-mat/klub/badge.svg?branch=master)](https://coveralls.io/github/auto-mat/klub?branch=master)

Instalace
============

Ke zprovoznění je zapotřebí následující

* Virtualenv
* Postgres 8.4 + postgis 1.5

Vzorová lokální konfigurace je v project/settings\_local\_sample.py, stačí přejmenovat na settings\_local.py a doplnit přístup k DB a SECRET\_KEY.

Instalace probíhá pomocí následujícíh příkazů:

* virtualenv --no-site-packages env
* env/bin/pip install distribute --upgrade
* sudo apt-get install libgraphviz-dev
* env/bin/pip install -r requirements
* cd apps/aklub && django-admin.py compilemessages -l "cs\_CZ"

Spuštění
============

Pro testovací účely spustíte projekt pomocí následujícího příkazu:

* env/bin/python manage.py runserver 0.0.0.0:8000
