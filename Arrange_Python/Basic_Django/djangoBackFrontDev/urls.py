from django.urls import path
from . import views


urlpatterns = [
	path('', views.djangoMain, name='mainpages'),
        path('inputPage.html', views.djangoInputpage, name='inputpage'),
        path('outPage.html', views.djangoOutputpage, name='outputpage'),
        
]
