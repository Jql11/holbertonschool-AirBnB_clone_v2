#!/usr/bin/python3
"""
Fabric script creates and distributes
an archive to web servers
"""
from fabric.api import env, put, run
import os.path
env.hosts = ['54.90.130.172', '52.90.163.197']


def do_deploy(archive_path):
    """
    Deploy archive to web server
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        get_name = archive_path.split("/")[-1]
        no_ext = get_name.split(".")[0]
        path_no_ext = "/data/web_static/releases/{}/".format(no_ext)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}".format(get_name, path_no_ext))
        run("rm /tmp/{}".format(get_name))
        run("mv {}web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}web_static".format(path_no_ext))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(path_no_ext, symlink))
        return True
    except Exception:
        return False
