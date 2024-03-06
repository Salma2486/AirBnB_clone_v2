#!/usr/bin/python3
""" Function that compress a folder """
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    local("mkdir -p versions")
    date = datetime.now()
    date_str = date.strftime("%Y%m%d%H%M%S")
    local("tar -cvzf versions/web_static_{}.tgz web_static".format(date_str))
    path = "versions/web_static_{}.tgz".format(date_str)
    if result.failed:
        return None
    else:
        return (path)
