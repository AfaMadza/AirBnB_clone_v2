#!/usr/bin/python3
"""
Creates and distributes an archive to your web servers
"""
import os
from fabric.operations import put
from fabric.api import run, env, hosts
from fabric import operations
from datetime import datetime, date


env.hosts = ["35.237.246.199", "35.196.144.206"]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/holberton'

def do_deploy(archive_path):
    """
    Uploads archive to /tmp/ directory of server and uncompresses
    the archive to a different folder whilst deleting un-needed files
    """
    if not os.path.exists(archive_path):
        return False
    arc_name = archive_path.split('/')[-1]
    arc_dir = arc_name.replace('.tgz', '')
    rem_path = '/tmp/' + arc_name
    if put(archive_path, rem_path).failed:
        return False
    run('mkdir -p /data/web_static/releases/{}/'.format(arc_dir))
    run('tar -zxf {} -C /data/web_static/releases/{}/'
        .format(rem_path, arc_dir))
    run('sudo rm {}'.format(rem_path))
    run('mv /data/web_static/releases/{}/web_static/* '
        '/data/web_static/releases/{}/'.format(arc_dir, arc_dir))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(arc_dir))
    run('rm -rf /data/web_static/current')
    run('sudo ln -sf /data/web_static/releases/{} /data/web_static/current'
        .format(arc_dir))
    print('New version deployed!')
    return True


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
        return file_
    except:
        return None


def deploy():
    """
    Creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
