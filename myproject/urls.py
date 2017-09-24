"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from myproject.views import hellodjango
from myproject.views import hello
from rest_framework import routers
import myproject
from snippets import views as snippets_views
from mongo_obj import views as mongo_views

router = routers.DefaultRouter()
router.register(r'users', myproject.views.UserViewSet)
router.register(r'groups', myproject.views.GroupViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hellodjango/$', hellodjango),
    url(r'^hello/$', hello),
    url(r'^service/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^snippets/$', snippets_views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippets_views.snippet_detail),
    url(r'^mongo/(?P<id>[0-9]+)/$', mongo_views.mongo_object),
]
