from django.urls import path

from.import views

urlpatterns=[
    path('',views.home,name='home'),
    path('ex',views.ex,name='ex'),
    #path('removepunc',views.removepunc,name='removepunc'),
    path('analyze',views.analyze,name='analyze'),
    path('download1',views.download1,name='download1'),
    


]