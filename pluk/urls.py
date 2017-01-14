from django.conf.urls import url
from pluk import views


urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^article/(?P<article_id>\d+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.show_article, name='article'),
    url(r'^pluk/register/$', views.register, name='register'),
    url(r'^pluk/login/$', views.user_login, name='login'),
    url(r'^pluk/restricted/', views.restricted, name='restricted'),
    url(r'^pluk/logout/$', views.user_logout, name='logout'),
    url(r'^article/(?P<article_id>\d+)/addlike/$', views.add_like, name='add_like'),
    url(r'^article/(?P<article_id>\d+)/adddislike/$', views.add_dislike, name='add_dislike'),

]
