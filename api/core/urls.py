"""dcms URL Configuration

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
from django.urls import path, include
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API Documents')

urlpatterns = [
    path('dadmin/', admin.site.urls),
    path('schemas/', schema_view),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/v1/', include('api_versioning.urls1', namespace='api_v1')),
    path('', include('apps.sr.urls', namespace='sr')),
]
