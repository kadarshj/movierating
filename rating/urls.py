"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from movie import views, apiviews


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^dashboard/$', views.home, name='home'),
    url(r'^mymovie/$', views.Mymovie, name= 'mymovie'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^subscribe/(?P<movie_id>[0-9]+)/movie_subscribe/(?P<user_id>[0-9]+)/$', views.SubscribeMovie, name='subscribe'),
    url(r'^ranking/$', views.Ranking, name= 'ranking'),

    url(r'^api/token/$',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    url(r'^api/token/refresh/$',TokenRefreshView.as_view(),name='token_refresh'),
    url(r'^api/movielist/$',apiviews.MovieListView.as_view()),
    url(r'^api/newsubscribe/', apiviews.SubscribeView.as_view()),
    url(r'^api/subscribelist/', apiviews.SubscribeListView.as_view()),
	url(r'^api/search/', apiviews.MovieListSearch.as_view()),
]
