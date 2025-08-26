from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.view_user_profile, name='view_user_profile'),
    path('account/update/', views.account_update, name='account_update'),
    path("password/change/",
         auth_views.PasswordChangeView.as_view(
            template_name="account/password_change.html",
            success_url="/password/change/done/"), name="password_change"),
    path("password/change/done/",
         auth_views.PasswordChangeDoneView.as_view(
             template_name="account/password_change_done.html"),
         name="password_change_done"),
    path(
        "password/reset/",
        auth_views.PasswordResetView.as_view(
            template_name="account/password_reset_form.html",
            email_template_name="account/password_reset_email.txt",
            html_email_template_name="account/password_reset_email.html",
            subject_template_name="account/password_reset_subject.txt",
            success_url=reverse_lazy("password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password/reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="account/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password/reset/confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password_reset_confirm.html",
            success_url=reverse_lazy("password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password/reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="account/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),

]
