# Django Imports
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# App Imports
from drops import views
from drops.views import AWizard
from drops.forms import Form1, Form2
from accounts import views as accounts_views

# Relative Imports
from . import views as open_views 


urlpatterns = [
    
    # Non-protected URLS
    url(r'^$', open_views.home, name='home'),
    url(r'^about/$', open_views.about, name='about'), 
    url(r'^contact/$', open_views.contact, name='contact'),   
    url(r'^signup/$', accounts_views.signup, name="signup"),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='open-pages/login.html'), name='login'),

    # Protected URLS
    url(r'^studio/$', views.studio, name="studio"),
    url(r'^create/$', views.create, name="create_drop"),
    url(r'^browse/$', views.browse, name="browse_area"),
    url(r'^dashboard/$', accounts_views.DashboardPageView.as_view(), name='dashboard'),
    url( r'drop/(?P<pk>\d+)/$', AWizard.as_view( [ Form1, Form2 ] ), name="drop_now" ),


    # Admin URL
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)