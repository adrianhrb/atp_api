runserver:
    python manage.py runserver

runserver0:
    python manage.py runserver 0.0.0.0:80

check:
    python manage.py check

shell:
    python manage.py shell

clean:
    find . -name '*.pyc' -exec rm {} \;

migrate app="":
    python manage.py migrate {{ app }}

makemigrations app="":
    python manage.py makemigrations {{ app }}

mmigrate app="":
    python manage.py makemigrations {{ app }} && python manage.py migrate {{ app }}

startapp app:
    #!/usr/bin/env bash
    python manage.py startapp {{ app }}
    APP_CLASS={{ app }}
    APP_CONFIG="{{ app }}.apps.${APP_CLASS^}Config"
    perl -0pi -e "s/(INSTALLED_APPS *= *\[)(.*?)(\])/\1\2    '$APP_CONFIG',\n\3/smg" $(find . -name settings.py)

super:
    python manage.py createsuperuser

dumpdata output:
    python manage.py dumpdata --indent=2 --output={{ output }}