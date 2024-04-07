#!/usr/bin/python3
#  this code generates a fabric script for the web-static
#  folder ofAirBnB  Clone repository
#  by using do_pack function
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """this designs a tar gzipped archive for web_static directory"""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
