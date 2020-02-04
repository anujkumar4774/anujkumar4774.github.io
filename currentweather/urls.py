
from django.urls import path
from . import views
app_name='currentweather'
urlpatterns = [path('',views.index,name='index'),
               path('currentweather/{}',views.cityinfo,name='cityname'),
               
]
