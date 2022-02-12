from django.urls import path
from .views.create_user_view import CreateUserView
from .views.create_token_view import CreateTokenView
from .views.manage_user_view import ManageUserView

app_name="user"

urlpatterns = [
    path("create", CreateUserView.as_view(), name="create"),
    path("token", CreateTokenView.as_view(), name="token"),
    path("me", ManageUserView.as_view(), name="me"),
]
