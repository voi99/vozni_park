from django.contrib.auth import logout
from django.urls import path,include

from . import views

urlpatterns = [
    path("",views.ChooseLoginView.as_view(),name='login-page'),
    path("employee-login",views.login_view,name='employee-login'),
    path("logout",views.logout_view,name="logout")
]
