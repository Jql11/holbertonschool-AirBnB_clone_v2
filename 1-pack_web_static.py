#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
import time


def do_pack():
    """all files in th folder are added to the archive"""
    current_time = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(current_time)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception:
        return None
