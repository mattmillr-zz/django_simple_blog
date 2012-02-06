from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'simple_blog.views.index', name='simple_blog_index'),
    url(r'^admin/', include(admin.site.urls)),
)
