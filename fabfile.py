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
    run('mkdir /home/deploy/apps/%(app_name)s/repo -p' % CONFIG)
    run('mkdir /home/deploy/apps/%(app_name)s/virtualenv -p' % CONFIG)
    run('mkdir /home/deploy/apps/%(app_name)s/releases -p' % CONFIG)
    
def config_vcs():
    global vcs_module
    if CONFIG['vcs'] == 'git':
        vcs_module = fab_git        
    elif CONFIG['vcs'] == 'hg':
        import fab_hg
        vcs_module = fab_hg

def create_database():
    sudo("mysql -u root --password=`cat /root/mysql_root_passwd` < /home/deploy/apps/%(app_name)s/repo/%(app_root_folder)s/conf/create_db.sql" % CONFIG)
    
def make_virtualenv():
    run ('virtualenv --no-site-packages /home/deploy/apps/%(app_name)s/virtualenv' % CONFIG)
    
def install():
    
    global CONFIG
    global vcs_module
    
    if not CONFIG['env']:
        abort("You must specify a Django environment to set up.")

    config_vcs()
    
    make_folders()
    vcs_module.clone()
    create_database()
    
    # syncdb and migrate !
    
    make_virtualenv()

def create_timestamp():
    now = datetime.now()
    CONFIG['dir_name'] = "%d-%02d-%02d-%02d-%02d-%02d" % (
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second
    )

def create_release_folder():
    run('mkdir /home/deploy/apps/%(app_name)s/releases/%(dir_name)s -p' % CONFIG)
    
def update_virtualenv():
    run('pip install -E /home/deploy/apps/%(app_name)s/virtualenv -r /home/deploy/apps/%(app_name)s/releases/%(dir_name)s/%(app_root_folder)s/requirements.txt' % CONFIG)
    
def update_symlink():
    run('ln -fs /home/deploy/apps/%(app_name)s/releases/%(dir_name)s /home/deploy/apps/%(app_name)s/current' % CONFIG)
    
def config_apache():
    sudo('cp /home/deploy/apps/%(app_name)s/repo/%(app_root_folder)s/conf/site_apache.conf /etc/apache2/sites-available/%(app_name)s.conf' % CONFIG)
    sudo('ln -fs /etc/apache2/sites-available/%(app_name)s.conf /etc/apache2/sites-enabled/%(app_name)s.conf' % CONFIG)
    sudo('/etc/init.d/apache2 restart')

def config_nginx():
    sudo('cp /home/deploy/apps/%(app_name)s/repo/%(app_root_folder)s/conf/site_nginx.conf /etc/nginx/sites-available/%(app_name)s.conf' % CONFIG)
    sudo('ln -fs /etc/nginx/sites-available/%(app_name)s.conf /etc/nginx/sites-enabled/%(app_name)s.conf' % CONFIG)
    sudo('/etc/init.d/nginx restart')
    
def deploy():
    
    global CONFIG
    global vcs_module
    
    if not CONFIG['env']:
        abort("You must specify a Django environment to set up.")

    config_vcs()
    
    create_timestamp()
    create_release_folder()
    
    vcs_module.update()
    vcs_module.export()
    
    # migrate ?
    
    update_virtualenv()

    update_symlink()
    config_apache()
    config_nginx()
