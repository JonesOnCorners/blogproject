"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.contrib import messages
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import auth_login, auth_logout, LoginView, LogoutView
from useraccounts.views import register, profile


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('register/',register, name='user-registration'),
    path('profile/',profile, name='user-profile'),
    path('login/',LoginView.as_view(template_name="useraccounts/login.html"), name='login'),
    path('logout/',LogoutView.as_view(template_name="useraccounts/logout.html") , name='logout'),
    path('',include('blog.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

