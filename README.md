# Django simple auth setup

## Dependencies

* django
* django-restframework

## Requirements

* py2 (django 1.11) py3 (django 2+)

## Get started

    # clone repository
    git clone https://github.com/sipp11/django-rest-auth-sample.git sample

    # create virtualenv and pull all dependencies
    cd sample
    mkvirtualenv sample
    pip install -r pip-dev.txt

    # populate database (sqlite as default)
    ./manage.py migrate

    # create user
    ./manage.py createsuperuser

    # run
    ./manage.py runserver

Then you can try logging in by using `curl`

    curl -XPOST 'http://localhost:8000/api-token-auth/' \
      -H "Content-Type: application/json" \
      -H 'Accept: application/json' -d \
      '{"username":"sipp11","password":"my-password"}'
