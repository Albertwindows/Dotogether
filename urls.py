from django.urls import path

from . import views
app_name='polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login,name='login'),
    path('detail/', views.detail, name='detail'),
    path('<int:pk>/results/', views.results, name='results'),
    path('profile/',views.profile,name='profile'),
    path('profile/submit',views.submit_activity,name='submit_activity'),
    path('profile/showinfo',views.showinfo,name='show_message'),
    path('profile/showactivities',views.show_activities,name='ground'),
    path('profile/myactivities',views.show_my_activities,name='my_activities'),
    path('profile/join',views.join_activity,name='join_activity'),

]