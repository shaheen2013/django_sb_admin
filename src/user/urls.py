from django.urls import path
# TODO:add app name for import views
from user.views import views, Authentication

urlpatterns = [
    path('', views.User.as_view(), name="user"),
    path('login/', Authentication.Login.as_view(), name="login"),
]
