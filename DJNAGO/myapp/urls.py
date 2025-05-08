from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index2/', views.index2, name='index2'),
    path('features2/', views.features2, name='features2'),
    path('business2/', views.business2, name='business2'),
    path('about_us2/', views.about_us2, name='about_us2'),
    path('inbox/', views.inbox, name='inbox'),
    path('upcoming/', views.upcoming, name='upcoming'),
    path('my_work/', views.my_work, name='my_work'),
    path('education/', views.education, name='education'),
    path('home2/', views.home2, name='home2'),
    path('business/', views.business, name='business'),
    path('features/', views.features, name='features'),
    path('about_us/', views.about_us, name='about_us'),
    path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('tasks/', views.tasks, name='tasks'),
    path('projects/', views.projects, name='projects'),
    path('calendar/', views.calendar, name='calendar'),

]



