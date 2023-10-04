from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("login_user/", views.login_user, name="login"),
    path("signUp_user/", views.signUp_user, name="signUp"),
    # If the name for this is just logout, it takes you to the Django administration logout page instead of redirecting
    # correctly
    path("logout_user/", views.logout_user, name="logout_user"),
    #path("password_reset/", auth_views.PasswordChangeView.as_view(template_name="registration/password_reset_form.html"),
         #name="password_reset"),
    path("password-reset/done/",
         auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
         name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>",
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),
         name="password_reset_confirm"),
]
