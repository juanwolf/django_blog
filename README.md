# juanwolf.fr

You can find here the code base of the website that you can find at https://juanwolf.fr.

## How to run it?

### Generate a .env file
```
$ cat .env
POSTGRES_USER=postgres
POSTGRES_DB=my_db
```

### RUN IT
```
docker-compose up
```

And normally the website should run on 127.0.0.1:8000 or docker_machine_ip:8000

Be aware that's just for testing purposes, do not use this in production. Well you could but I would recommand to use a proper orchestration tool such as nomad or ansible to manage your containers. It would sucks if you run one postgres container for each application running on your docker host.

### Create the DB (optionnal)

In case your postgres container is fresh or you want a new db, create a new db with this command:

```
docker run -it --rm --link the_db_container_launched:postgres \
 --net=the_network_created_for_your_docker_compose \
 postgres psql -h postgres -U postgres
```

And once in the container:

`postgres=# CREATE DATABASE my_db;`

2ez

### Applying migrations

To modificate the postgres container with our migration we need to apply the migrations INSIDE the docker container.

`docker-compose run django /opt/virtualenvs/juanwolf_fr/bin/python manage.py migrate`

### Create a superuser

To be able to access to the admin section of this website you must create an admin user.

`docker-compose run django /opt/virtualenvs/juanwolf_fr/bin/python manage.py createsuperuser`

Go to localhost:8000/admin and you should be able to log on with the credentials you provided.


## ENVIRONMENT VARIABLES

The following environment variables are available to setup:

| Name              |   Default Value     | Type expected  |
|-------------------|---------------------|----------------|
| SECRET_KEY        |  qwerty1234567890   | String         |
| DEBUG             |  False              | Boolean        |
| DTABASE_USER      |  postgres           | String         |
| DATABASE_NAME     |  postgres           | String         |
| DATABASE_HOST     |  ''                 | String         |
| DATABASE_PASSWORD | ''                  | String         |
| SENTRY_PROTOCOL   | ''                  | String         |
| SENTRY_USER       | ''                  | String         |
| SENTRY_PASSWORD   | ''                  | String         |
| SENTRY_URL        | ''                  | String         |

## License

This work is under [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/)

