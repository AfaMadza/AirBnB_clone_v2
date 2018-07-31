#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder
"""
from fabric import operations
from datetime import datetime, date
import os


def do_pack():
    """
    Generate a tgz file in the local server
    """
    curr_time = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file_ = "versions/web_static_{}.tgz".format(curr_time)
    msg = ''
    msg += operations.local('mkdir -p versions')
    msg += operations.local('tar -czvf {} web_static'.format(file_))
    file_size = os.stat('{}'.format(file_)).st_size
    output = 'web_static packed: versions/{} -> {}'.format(file_, file_size)
    try:
        print(output+'Bytes')
    except:
        return None
