import os, sys, site

site.addsitedir('/home/deploy/apps/simpleblog/virtualenv/lib/python2.6/site-packages')

sys.path.insert(0, "/home/deploy/apps/simpleblog/current")
sys.path.insert(0, "/home/deploy/apps/simpleblog/current/django_simple_blog")
sys.path.insert(0, "/home/deploy/apps/simpleblog/virtualenv/lib/python2.6/site-packages")

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_simple_blog.settings'

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
