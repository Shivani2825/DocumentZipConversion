from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.registrationpage, name="registrationpage"),
    path('reg-data/', views.signup, name='reg-data'),
    path('loginpage/', views.loginpage,name='loginpage'),
    path('login/', views.login, name='login'),
    path('upload-file/', views.upload_files),
    path('upload-files-data/', views.upload_files_data),
    path('download_files/<int:user_id>/',views.download_files_as_zip, name='download_files'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
