from django.conf.urls import patterns, include, url
from django.contrib import admin
from website import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
)

