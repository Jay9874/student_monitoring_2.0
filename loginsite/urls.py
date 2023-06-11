from . import views
from django.urls import path


urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("forgot", views.forgot, name="forgot")
]
