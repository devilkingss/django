from django.urls import path
from . import views

urlpatterns= [

          path('',views.index,name='index'),
          path('watch.html',views.watch,name='watch'),
          path('index.html',views.watch,name='index.html')
      ]