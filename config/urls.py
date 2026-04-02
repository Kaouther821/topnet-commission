from django.contrib import admin
from django.urls import path
from accounts.views import login_view, logout_view
from core.views import home
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home, name='home'),
    path('otp/', TemplateView.as_view(template_name='accounts/otp_verify.html'), name='otp'),
    path('change-password/', TemplateView.as_view(template_name='accounts/change_password.html'), name='change_password'),
    path('blocked/', TemplateView.as_view(template_name='accounts/blocked.html'), name='blocked'),
    path('dashboard/', TemplateView.as_view(template_name='dashboard/dashboard.html'), name='dashboard'),
    path('users/', TemplateView.as_view(template_name='accounts/users_list.html'), name='users'),
    path('import-csv/', TemplateView.as_view(template_name='accounts/import_csv.html'), name='import_csv'),
    path('logs/', TemplateView.as_view(template_name='audit/logs_list.html'), name='logs'),
]