from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('preference_spectrum/', views.preference_spectrum, name='preference_spectrum'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/delete/<delete_id>', views.tasks, name='tasks'),
]
