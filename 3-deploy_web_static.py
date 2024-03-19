#!/usr/bin/python3
from fabric.api import local, env, put, run
from time import strftime
from datetime import date
from os.path import exists


env.hosts = ['35.174.205.47', '54.87.158.254']
env.user = 'ubuntu'


def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        print("An error occurred during packing:", e)
        raise None


def do_deploy(archive_path):
    """Fabric script that distributes
    an archive to your web server"""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[-1]
        name = filename.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename, name))
        run("rm /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        print("New version deployed!")
        return True
    except Exception as e:
        print("An error occurred:", e)
        return False


def deploy():
    """run the 2 functions"""
    path = do_pack()
    if not path:
        return False
    return do_deploy(path)
