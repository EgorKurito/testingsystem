from django.urls import path

from app import views

app_name = 'app'
auth_patterns = [
    path('signup/', views.signup, name='signup')
]

test_patterns = [
    path('test/<int:pk>/question/<int:q>/', views.test_view, name='test'),
    path('test/<int:pk>/finish/', views.finish, name='finish'),
    path('', views.HomeView.as_view(), name='home'),
]

urlpatterns = auth_patterns + test_patterns
