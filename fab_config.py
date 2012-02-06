from fabric.api import env

CONFIG = {}
CONFIG['env'] = None

CONFIG['app_name'] = 'simpleblog'
CONFIG['app_root_folder'] = 'django_simple_blog'

CONFIG['vcs'] = 'git'
CONFIG['git_repo'] = 'git://github.com/mattmillr/django_simple_blog.git'

def bksw1():
    global CONFIG
    env.hosts = ['66.228.46.218',]
    CONFIG['env'] = 'dev'
    
