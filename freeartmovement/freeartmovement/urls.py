"""freeartmovement URL Configuration

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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from drops import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from . import views as open_views 


urlpatterns = [
    url(r'^$', open_views.home, name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='open-pages/login.html'), name='login'),
    url(r'^dashboard/$', accounts_views.dashboard, name="dashboard"),
    url(r'^signup/$', accounts_views.signup, name="signup"),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^studio/$', views.studio, name="studio"),
    url(r'^create/$', views.create, name="create_drop"),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)