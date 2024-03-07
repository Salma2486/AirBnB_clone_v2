#!/usr/bin/python3
from fabric.api import env, put, run
from os.path import exists


env.hosts = ['54.174.5.167', '18.210.10.255']


def do_deploy(archive_path):
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
        run("mv /data/web_static/releases/{}/web_static/* /data/\
                web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        print("New version deployed!")
        return True
    except Exception as e:
        return False
