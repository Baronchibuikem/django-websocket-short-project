## About project

A simple project to test out websocket in django, utilizing celery, redis and retrieving data from a thirdparty library while updating the page automatically without refreshing

## To run the project

        git clone https://github.com/Baronchibuikem/django-websocket-short-project
        pip install -r requirements
        python manage.py makemigrations
        python manange.py migrate
        python manage.py collectstatic
        python manage.py runserver
        celery -A newsaggregator worker -l INFO
        celery -A newsaggregator beat -INFO

Since we are using a scheduler, once you start your django server, you will need to open 2 other terminals to run the celery tasks(the last two commands above).

Navigate to your localhost and you should see the data updating automatically every 3 seconds
