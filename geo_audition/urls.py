"""geo_audition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
]

SchemaView = get_schema_view(openapi.Info(
    title=_("Audition API"),
    default_version='v1',
    description=_("Audition description of API.")),
    public=True,
    permission_classes=(permissions.AllowAny,), )

urlpatterns += [
    path('', include('apps.phonebook.urls')),
    path('', include('apps.services.urls')),
    path('', include('apps.switchboard.urls')),
    path('', include('apps.calls.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.user_action.urls')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('webapi/admin/', admin.site.urls),
    path('webapi/swagger.json', SchemaView.without_ui(cache_timeout=0), name='schema-json'),
    path('webapi/swagger/', SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('webapi/redoc/', SchemaView.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
