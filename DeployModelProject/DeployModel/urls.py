
from django.contrib import admin
from django.urls import path, include

from Project import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.Home, name='home'),
    path('result', views.result, name = 'result'),
    
    # path('', include('Project.urls')),
    
]

#urlpatterns = [
 #  path('', views.Home, name='home'),
#    path('index/',views.result, name='index'),
    
#]
