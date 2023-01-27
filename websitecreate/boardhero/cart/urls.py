"""cart URL Configuration

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
from cartapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('detail/<int:productid>/', views.detail),
    path('addtocart/<str:ctype>/', views.addtocart),
    path('addtocart/<str:ctype>/<int:productid>/', views.addtocart),
    path('cart/', views.cart),
    path('cartorder/', views.cartorder),
    path('cartok/', views.cartok),
    path('cartordercheck/', views.cartordercheck),
    path('sellpeoplelogin/', views.sellpeoplelogin),
    path('sellpeoplecreate/', views.sellpeoplecreate),
    path('create/',views.create),
    path('adminmain/', views.adminmain),
    path('adminadd/', views.adminadd),
    path('login/', views.login),
    path('logout/', views.logout),
    path('adminfix/<int:albumid>/', views.adminfix),
    path('adminfix/<int:albumid>/<int:photoid>/', views.adminfix),
    path('adminfix/<int:albumid>/<int:photoid>/<str:deletetype>/', views.adminfix),
    path('albumshow/<int:albumid>/', views.albumshow),
    path('albumphoto/<int:photoid>/<int:albumid>/', views.albumphoto),
    path('adminmain/<int:albumid>/', views.adminmain),
    path('index2/', views.index2),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)