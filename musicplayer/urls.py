from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('rule', views.rule, name='rule'),
    path('streamlit/', views.streamlit_view, name = 'streamlit_view')
    
]

