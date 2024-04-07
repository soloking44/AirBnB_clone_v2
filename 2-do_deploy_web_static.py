#!/usr/bin/python3
# this is a fabric script that 
# runs properties of web_static
# by using do_pack func 
import os
from fabric.api import run, put, env

env.hosts = ['34.204.60.80', '54.160.72.183']
env.user = "ubuntu"


def do_deploy(archive_path):
    """this designs the directory web_static."""
    if os.path.exists(archive_path) is False:
        return False
    else:
        try:
            put(archive_path, "/tmp/")
            file_name = archive_path.split("/")[1]
            file_name2 = file_name.split(".")[0]
            final_name = "/data/web_static/releases/" + file_name2 + "/"
            run("mkdir -p " + final_name)
            run("tar -xzf /tmp/" + file_name + " -C " + final_name)
            run("rm /tmp/" + file_name)
            run("mv " + final_name + "web_static/* " + final_name)
            run("rm -rf " + final_name + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + final_name + " /data/web_static/current")
            print("New version deployed!")
            return True
        except Exception as e:
            print("Error:", e)
            return False
