# juanwolf.fr

You can find here the code base of the website that you can find at https://juanwolf.fr.

# How to run it ?

```
docker-compose up
```

And normally the website should run on 127.0.0.1:8000

## Applying migrations

To modificate the postgres container with our migration we need to apply the migrations INSIDE the docker container.
For that:

`docker-compose run django /opt/virtualenvs/juanwolf_fr/bin/python manage.py migrate`

