from fabric.api import env

CONFIG = {}
CONFIG['env'] = None

CONFIG['app-name'] = 'simpleblog'
CONFIG['app-root-folder'] = 'django_simple_blog'

CONFIG['vcs'] = 'git'
CONFIG['git-repo'] = 'git://github.com/mattmillr/django_simple_blog.git'
CONFIG['repo-name'] = 'django_simple_blog'

def bksw1():
    global CONFIG
    env.hosts = ['66.228.46.218',]
    CONFIG['env'] = 'dev'
    
