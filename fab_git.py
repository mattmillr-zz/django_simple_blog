from __future__ import with_statement
from fabric.api import env, run, cd
from fab_config import *

def clone():
    run('git clone %(git_repo)s /home/deploy/apps/%(app_name)s/repo/%(app_root_folder)s' % CONFIG)
    
    
def update():
    with cd('/home/deploy/apps/%(app_name)s/repo/%(app_root_folder)s' % CONFIG):
        run('git pull')
        
def export():
    run('cp -R /home/deploy/apps/%(app_name)s/repo/%(app_root_folder)s /home/deploy/apps/%(app_name)s/releases/%(dir_name)s/%(app_root_folder)s' % CONFIG)
    run('rm -rf /home/deploy/apps/%(app_name)s/releases/%(dir_name)s/%(app_root_folder)s/.git' % CONFIG)
