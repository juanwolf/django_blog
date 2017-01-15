#!/bin/python

import argparse
from subprocess import call


def update_database(docker_image, database_container_name):
    call(
        ["docker", "run", "--rm",
            "--net=container:%s" % database_container_name,
            docker_image,
            "/opt/virtualenvs/juanwolf_fr/bin/python",
            "/opt/juanwolf_fr/juanwolf_fr/manage.py",
            "migrate"]
    )


def update_translations(docker_image):
    call(["docker", "run", "--rm", docker_image,
        "/opt/virtualenvs/juanwolf_fr/bin/python",
        "/opt/juanwolf_fr/juanwolf_fr/manage.py",
        "compilemessages"])  # noqa


def update_staticfiles(docker_image, local_volume):
    call(["docker", "run", "--rm", "--volume=%s:/srv/http/static" % local_volume.strip(),
            docker_image, "/opt/virtualenvs/juanwolf_fr/bin/python",
            "/opt/juanwolf_fr/juanwolf_fr/manage.py",
            "collectstatic", "--noinput"]) # noqa


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Update all the third party of this django app."
    )
    parser.add_argument(
        "docker_image",
        type=str,
        help="The name of the docker image that you're using for this application"
    )
    parser.add_argument(
        "database_container_name",
        type=str,
        help="The name of the container that you're using for the database "
        "of this application"
    )
    parser.add_argument(
        "local_volume",
        type=str,
        help="The location where you want to store the staticfiles. "
        "(/srv/http/static)"
    )
    args = parser.parse_args()

    update_staticfiles(args.docker_image, args.local_volume)
    update_database(args.docker_image, args.database_container_name)
    update_translations(args.docker_image)
