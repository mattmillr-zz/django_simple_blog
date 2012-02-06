from datetime import datetime
from fabric.api import env, run, sudo
from fabric.utils import abort
from fabric.context_managers import settings

env.user = 'deploy'
vcs_module = None

from fab_config import *
import fab_git
import fab_hg

def make_folders():
    run('mkdir /home/deploy/apps/%(app-name)s/repo -p' % CONFIG)
    run('mkdir /home/deploy/apps/%(app-name)s/virtualenv -p' % CONFIG)
    
def config_vcs():
    global vcs_module
    if CONFIG['vcs'] == 'git':
        vcs_module = fab_git        
    elif CONFIG['vcs'] == 'hg':
        import fab_hg
        vcs_module = fab_hg

def create_database():
    sudo("mysql -u root --password=`cat /root/mysql_root_passwd` < /home/deploy/apps/%(app-name)s/repo/%(app-root-folder)s/conf/create_db.sql" % CONFIG)
    
def make_virtualenv():
    run ('virtualenv --no-site-packages /home/deploy/apps/%(app-name)s/virtualenv' % CONFIG)
    
def install():
    
    global CONFIG
    global vcs_module
    
    if not CONFIG['env']:
        abort("You must specify a Django environment to set up.")

    config_vcs()
    
    make_folders()
    vcs_module.clone()
    create_database()
    make_virtualenv()
    
    
def deploy():
    # config timestamp
    # pull & update repo on server
    # copy files to release dir
    # update virtualenv dependencies
    # symlink current --> release
    # copy apache config
    # copy nginx confi
    # reload apache
    # restart nginx
    pass