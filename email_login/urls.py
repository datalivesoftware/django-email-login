# We need to override login view, the rest is ok.
from django.conf.urls import url
from django.contrib.auth.urls import urlpatterns as auth_urls
from forms import EmailAuthenticationForm

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'email_login/login.html',
         'authentication_form': EmailAuthenticationForm}, name='auth_login'),
]

urlpatterns += auth_urls
