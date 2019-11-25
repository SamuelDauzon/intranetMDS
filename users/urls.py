from django.urls import path
# Import du module views de l'application users
from users import views

app_name = 'users'

urlpatterns = [
    path(r'hello/', views.hello, name="hello"),

    path('register/', views.register, name="register"),

    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_view, name="login"),

]