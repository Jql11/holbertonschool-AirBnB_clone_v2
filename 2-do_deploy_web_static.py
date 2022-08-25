#!/usr/bin/python3
"""distributes an archive to server using function do_deploy
"""
from fabric.api import put
from os.path import exists


def do_deploy(archive_path):
    """distributing archive to server"""
    if exists(archive_path) is False:
        return False
    try:
        get_name = archive_path.split("/")[-1]
        no_ext = get_name.split(".")[0]
        folder_path = "/data/web_static/releases/{}/".format(no_ext)
        put("archive_path", "/tmp")
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp{} -C {}/".format(get_name, folder_path))
        run("rm /tmp/{}".format(get_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        return True
    except Exception:
        return False
