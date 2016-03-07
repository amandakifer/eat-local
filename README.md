# eat-local
Find local deals on yelp.


### Environment variables

Must set the following environment variables

    DJANGO_SECRET_KEY  # Required on server only
    DJANGO_DEBUG  # Required for local dev only
    DATABASE_URL  # Required for local dev only
    YELP_CONSUMER_KEY
    YELP_CONSUMER_SECRET
    YELP_TOKEN
    YELP_TOKEN_SECRET

To set an environment variable on Heroku, e.g.:

    $ heroku config:set DJANGO_DEBUG=0

To set an environment variable locally using the terminal, e.g.:

    $ export DJANGO_DEBUG=0

To set an environment variable locally for a virtualenv, e.g.:

    $ vim ~/.virtualenvs/eat-local/bin/activate

    Add the following line at the bottom of the script and save:
    export DJANGO_DEBUG=0

    $ workon eat-local
