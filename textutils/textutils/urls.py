"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

# PART - 1
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'), # No extension, index function from views file, name is set to index
#     path('about/', views.about, name='about'), # Add "/about/" at last of url provided while running server, about function from views file, name is set to about
#     path('quote/', views.quote, name='quote'), # Add "/quote/" at last of url provided while running server, quote function from views file, name is set to quote
#     path('mostUsedLinks/', views.mostUsedLinks, name='mostUsedLinks'), # Add "/mostUsedLinks/" at last of url provided while running server, mostUsedLinks function from views file, name is set to mostUsedLinks
#     path('gallery/', views.gallery, name='gallery'),
#     path('services/', views.services, name='services'),
#     path('contact/', views.contact, name='contact')
# ]

# PART - 2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]