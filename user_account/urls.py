from django.urls import path
from user_account.views.UserView import LoginAPI, RegisterAPI


urlpatterns = [
    path(
        'signin',
        LoginAPI.as_view(),
        name='account_signin'
    ),

    path(
        'signup',
        RegisterAPI.as_view(),
        name='account_signup'
    ),

]
