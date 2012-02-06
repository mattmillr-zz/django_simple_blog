from fabric.api import env, run
from fab_config import *

def clone():
    run('git clone %(git-repo)s /home/deploy/apps/%(app-name)s/repo/%(app-root-folder)s' % CONFIG)
    
    
def update():
    pass
    
def export():
    pass