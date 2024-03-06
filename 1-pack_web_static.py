#!/usr/bin/python3
""" srgt sryt hrsdy thrdsyth6d"""
from fabric.api import local
import os.path
from datetime import datetime


def do_pack():
    """rftxh srt hsrdt hf"""
    local("mkdir -p versions")
    date = datetime.now()
    date_str = date.strftime("%Y%m%d%H%M%S")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static".format(date_str))
    path = "versions/web_static_{}.tgz".format(date_str)
    if result.failed:
        return None
    else:
        return (path)
